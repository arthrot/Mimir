#!/usr/bin/env python3
"""Monte Carlo business-model comparison for the Moolah opportunity research.

The distributions are explicit planning assumptions, not empirical forecasts.
Run with Python 3 and NumPy; outputs are deterministic under SEED.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path

import numpy as np


SEED = 20261105
N_SIMS = 100_000
MONTHS = 12
OUT = Path(__file__).resolve().parent


def tri(rng: np.random.Generator, lo: float, mode: float, hi: float, size: int) -> np.ndarray:
    return rng.triangular(lo, mode, hi, size=size)


MODELS = {
    "Supplier/import ops": {
        "kind": "sales",
        "fit_probability": 0.55,
        "conversations": (10, 20, 34),
        "monthly_lead_growth": (-0.01, 0.025, 0.07),
        "close_rate_beta": (3.0, 22.0),
        "sales_cycle_months": (0, 1, 2),
        "setup_fee": (2500, 6000, 12000),
        "monthly_fee": (1200, 2800, 5500),
        "monthly_churn_beta": (2.0, 70.0),
        "gross_margin": (0.52, 0.68, 0.82),
        "initial_capacity": 12,
        "scaled_capacity": 28,
        "scale_month": 6,
        "scale_probability": 0.60,
    },
    "GovCon response ops": {
        "kind": "sales",
        "fit_probability": 0.45,
        "conversations": (8, 16, 28),
        "monthly_lead_growth": (-0.01, 0.02, 0.06),
        "close_rate_beta": (2.5, 25.0),
        "sales_cycle_months": (1, 2, 3),
        "setup_fee": (1000, 3000, 7000),
        "monthly_fee": (900, 2000, 4000),
        "monthly_churn_beta": (2.0, 55.0),
        "gross_margin": (0.58, 0.74, 0.86),
        "initial_capacity": 18,
        "scaled_capacity": 45,
        "scale_month": 6,
        "scale_probability": 0.68,
    },
    "AI governance evidence": {
        "kind": "sales",
        "fit_probability": 0.35,
        "conversations": (4, 9, 18),
        "monthly_lead_growth": (-0.02, 0.015, 0.05),
        "close_rate_beta": (2.0, 22.0),
        "sales_cycle_months": (2, 3, 5),
        "setup_fee": (6000, 14000, 28000),
        "monthly_fee": (2200, 4800, 9000),
        "monthly_churn_beta": (1.5, 75.0),
        "gross_margin": (0.48, 0.64, 0.78),
        "initial_capacity": 9,
        "scaled_capacity": 20,
        "scale_month": 7,
        "scale_probability": 0.50,
    },
    "Atlassian compliance app": {
        "kind": "app",
        "fit_probability": 0.25,
        "launch_month": (2, 4, 6),
        "monthly_visitors": (180, 550, 1800),
        "monthly_traffic_growth": (-0.02, 0.045, 0.13),
        "trial_rate_beta": (3.0, 55.0),
        "trial_to_paid_beta": (3.0, 13.0),
        "monthly_arpa": (55, 180, 650),
        "monthly_churn_beta": (3.0, 48.0),
        "gross_margin": (0.72, 0.86, 0.94),
    },
}


def simulate_sales(rng: np.random.Generator, p: dict) -> dict[str, np.ndarray]:
    n = N_SIMS
    base_conversations = tri(rng, *p["conversations"], n)
    lead_growth = tri(rng, *p["monthly_lead_growth"], n)
    close_rate = rng.beta(*p["close_rate_beta"], size=n)
    cycle = np.rint(tri(rng, *p["sales_cycle_months"], n)).astype(int)
    setup_fee = tri(rng, *p["setup_fee"], n)
    monthly_fee = tri(rng, *p["monthly_fee"], n)
    churn = rng.beta(*p["monthly_churn_beta"], size=n)
    margin = tri(rng, *p["gross_margin"], n)
    scales = rng.random(n) < p["scale_probability"]

    active = np.zeros(n, dtype=int)
    revenue = np.zeros(n)
    gross_profit = np.zeros(n)
    pending = [np.zeros(n, dtype=int) for _ in range(MONTHS + 6)]

    for month in range(MONTHS):
        retained = rng.binomial(active, 1 - churn)
        capacity = np.full(n, p["initial_capacity"], dtype=int)
        if month >= p["scale_month"]:
            capacity = np.where(scales, p["scaled_capacity"], capacity)
        starts_now = np.minimum(pending[month], np.maximum(capacity - retained, 0))
        active = retained + starts_now

        conversations = np.maximum(
            0,
            rng.poisson(base_conversations * np.power(1 + lead_growth, month)),
        )
        wins = rng.binomial(conversations, close_rate)
        committed_future = np.sum(np.stack(pending[month + 1 :], axis=0), axis=0)
        room = np.maximum(capacity - active - committed_future, 0)
        wins = np.minimum(wins, room)
        start_month = month + cycle
        valid = start_month < MONTHS
        for lag in np.unique(cycle[valid]):
            mask = valid & (cycle == lag)
            if lag == 0:
                active[mask] += wins[mask]
                starts_now[mask] += wins[mask]
            else:
                pending[month + int(lag)][mask] += wins[mask]

        monthly_revenue = active * monthly_fee + starts_now * setup_fee
        revenue += monthly_revenue
        gross_profit += monthly_revenue * margin

    ending_mrr = active * monthly_fee
    return {
        "revenue": revenue,
        "gross_profit": gross_profit,
        "ending_mrr": ending_mrr,
        "customers": active.astype(float),
    }


def simulate_app(rng: np.random.Generator, p: dict) -> dict[str, np.ndarray]:
    n = N_SIMS
    launch = np.rint(tri(rng, *p["launch_month"], n)).astype(int)
    visitors = tri(rng, *p["monthly_visitors"], n)
    growth = tri(rng, *p["monthly_traffic_growth"], n)
    trial_rate = rng.beta(*p["trial_rate_beta"], size=n)
    paid_rate = rng.beta(*p["trial_to_paid_beta"], size=n)
    arpa = tri(rng, *p["monthly_arpa"], n)
    churn = rng.beta(*p["monthly_churn_beta"], size=n)
    margin = tri(rng, *p["gross_margin"], n)

    active = np.zeros(n, dtype=int)
    revenue = np.zeros(n)
    gross_profit = np.zeros(n)
    for month in range(MONTHS):
        active = rng.binomial(active, 1 - churn)
        live = month >= launch
        traffic = np.where(live, rng.poisson(visitors * np.power(1 + growth, np.maximum(month - launch, 0))), 0)
        trials = rng.binomial(traffic, trial_rate)
        active += rng.binomial(trials, paid_rate)
        monthly_revenue = active * arpa
        revenue += monthly_revenue
        gross_profit += monthly_revenue * margin

    return {
        "revenue": revenue,
        "gross_profit": gross_profit,
        "ending_mrr": active * arpa,
        "customers": active.astype(float),
    }


def apply_fit_risk(rng: np.random.Generator, values: dict[str, np.ndarray], fit_probability: float) -> dict[str, np.ndarray]:
    """Include the chance that the initial niche/offer never validates.

    Failed validation is not assumed to mean exactly zero: founders may collect a
    little pilot revenue before killing or pivoting. The 2%-25% salvage range is
    deliberately explicit and should be replaced with observed funnel data.
    """
    fits = rng.random(N_SIMS) < fit_probability
    salvage = tri(rng, 0.02, 0.10, 0.25, N_SIMS)
    multiplier = np.where(fits, 1.0, salvage)
    return {key: val * multiplier for key, val in values.items()}


def summarize(name: str, conditional: dict[str, np.ndarray], risk_adjusted: dict[str, np.ndarray]) -> dict:
    values = risk_adjusted
    rev = values["revenue"]
    mrr = values["ending_mrr"]
    return {
        "idea": name,
        "conditional_revenue_p50": round(float(np.percentile(conditional["revenue"], 50))),
        "revenue_p10": round(float(np.percentile(rev, 10))),
        "revenue_p50": round(float(np.percentile(rev, 50))),
        "revenue_p90": round(float(np.percentile(rev, 90))),
        "gross_profit_p50": round(float(np.percentile(values["gross_profit"], 50))),
        "ending_mrr_p50": round(float(np.percentile(mrr, 50))),
        "ending_customers_p50": round(float(np.percentile(values["customers"], 50)), 1),
        "prob_revenue_100k": round(float(np.mean(rev >= 100_000)), 4),
        "prob_revenue_500k": round(float(np.mean(rev >= 500_000)), 4),
        "prob_revenue_1m": round(float(np.mean(rev >= 1_000_000)), 4),
        "prob_exit_arr_1m": round(float(np.mean(mrr * 12 >= 1_000_000)), 4),
    }


def main() -> None:
    rng = np.random.default_rng(SEED)
    results = {}
    summaries = []
    for name, params in MODELS.items():
        conditional = simulate_sales(rng, params) if params["kind"] == "sales" else simulate_app(rng, params)
        values = apply_fit_risk(rng, conditional, params["fit_probability"])
        results[name] = values
        summaries.append(summarize(name, conditional, values))

    with (OUT / "simulation_summary.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=summaries[0].keys())
        writer.writeheader()
        writer.writerows(summaries)

    assumptions = {
        "seed": SEED,
        "simulations": N_SIMS,
        "months": MONTHS,
        "currency": "USD",
        "warning": "Planning assumptions only; probabilities are conditional on these distributions.",
        "models": MODELS,
    }
    (OUT / "simulation_assumptions.json").write_text(json.dumps(assumptions, indent=2) + "\n")

    sensitivity_rows = []
    for name, values in results.items():
        base = float(np.median(values["revenue"]))
        # Transparent first-order sensitivities around the simulated base outcome.
        for factor, multiplier in [
            ("lead flow / marketplace traffic -25%", 0.75),
            ("base assumptions", 1.00),
            ("lead flow / marketplace traffic +25%", 1.25),
            ("pricing -25%", 0.75),
            ("pricing +25%", 1.25),
        ]:
            sensitivity_rows.append({"idea": name, "scenario": factor, "estimated_median_revenue": round(base * multiplier)})
    with (OUT / "sensitivity_summary.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=sensitivity_rows[0].keys())
        writer.writeheader()
        writer.writerows(sensitivity_rows)

    print(json.dumps(summaries, indent=2))


if __name__ == "__main__":
    main()
