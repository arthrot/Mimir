# First-year business-model simulation

_Run date: 2026-11-05. Currency: USD. Horizon: 12 months. These are planning scenarios, not empirical forecasts or income promises._

## Conclusion

The supplier/import-operations service is the strongest first test for two Singapore-based technical founders. In the risk-adjusted model it has the highest median revenue, gross profit, and probability of crossing $100k or $500k in recognized first-year revenue. The Atlassian app is attractive as a later distribution layer, but weak as the initial cash engine.

The largest determinant is not model cost or coding output. It is whether the founders validate a painful niche and establish repeatable distribution. To represent that, the simulation includes a subjective “initial offer validates” probability; failed attempts retain only 2–25% of the corresponding execution-case revenue before a kill or pivot. This assumption must be replaced by real paid-pilot results.

## Results from 100,000 runs

| Idea | Median if offer validates | Risk-adjusted revenue P10 | Median | P90 | Median gross profit | P($100k+) | P($500k+) | P($1M+) | P(exit ARR $1M+) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Supplier/import operations | $467k | $30k | **$214k** | $696k | **$143k** | **60.3%** | **24.2%** | **1.33%** | **8.98%** |
| GovCon response operations | $209k | $9k | $52k | $349k | $38k | 37.0% | 3.16% | 0.01% | 1.39% |
| AI-governance evidence | $243k | $6k | $44k | $368k | $27k | 29.2% | 3.99% | 0.02% | 0.68% |
| Atlassian compliance app | $54k | $1k | $9k | $76k | $8k | 7.31% | 0.28% | 0.02% | 0.61% |

The small $1M probabilities are the honest result: collecting $1M in the first year is a tail event even under fairly aggressive execution assumptions. Supplier/import operations wins because service onboarding fees and higher recurring prices monetize a small number of clients; the app needs much more distribution before its margin advantage matters.

## Main assumptions

| Idea | Initial-offer validation | Qualified conversations or traffic | Price assumption | Typical sales cycle | Initial capacity |
|---|---:|---|---|---|---:|
| Supplier/import operations | 55% | 10–34 conversations/month | $2.5k–$12k setup + $1.2k–$5.5k/month | 0–2 months | 12 clients |
| GovCon response operations | 45% | 8–28 conversations/month | $1k–$7k setup + $0.9k–$4k/month | 1–3 months | 18 clients |
| AI-governance evidence | 35% | 4–18 conversations/month | $6k–$28k assessment + $2.2k–$9k/month | 2–5 months | 9 clients |
| Atlassian compliance app | 25% | 180–1,800 listing visitors/month after launch | $55–$650 monthly account revenue | launch in month 2–6 | software-led |

The validation probabilities, funnel rates, and price ranges are judgment assumptions. Marketplace size, regulatory timing, and platform economics are sourced in the main opportunity report, but none of those facts proves that this team can acquire customers at these rates.

## Sensitivity

A first-order ±25% change in lead flow or pricing moves median modeled revenue by approximately the same percentage before second-order capacity and conversion effects:

| Idea | -25% scenario | Base median | +25% scenario |
|---|---:|---:|---:|
| Supplier/import operations | $161k | $214k | $268k |
| GovCon response operations | $39k | $52k | $65k |
| AI-governance evidence | $33k | $44k | $54k |
| Atlassian compliance app | $7k | $9k | $12k |

Fit risk is more important than either perturbation. If the supplier/import offer's validation probability is materially below 50%, its median collapses toward small-pilot revenue. The immediate job is therefore to estimate real validation and conversion rates, not to tune the software architecture.

## Four live tests

### 1. Supplier/import operations — run first

- Target: Singapore/Malaysia freight forwarders, importers, and equipment distributors with 10–100 employees.
- Offer: fixed-scope document and quote workflow diagnostic, followed by a 14-day pilot.
- Test corpus: at least 100 historical emails/documents from consenting design partners.
- Pass gates: 30 qualified conversations; 10 artifact-sharing interviews; at least 3 paid diagnostics at S$2k+; 2 pilot renewals; at least 50% cycle-time reduction; at least 95% field-level extraction accuracy; every material exception traceable to source documents.
- Kill/pivot: fewer than 2 paid pilots after 30 qualified conversations, no measurable time/error reduction, or every customer requires a different workflow.

### 2. GovCon response operations

- Target: one US contractor category, not all federal vendors.
- Offer: weekly bid/no-bid memo and compliance matrix sourced from SAM.gov documents.
- Backtest: 20 historical solicitations and the customer's past bid decisions.
- Pass gates: at least 95% recall on mandatory requirements; zero invented clauses; 3 paid trials from 25 qualified firms; buyers report at least 5 analyst hours saved per week.
- Kill/pivot: the value is only email alerts, or customers will not pay at least $1k/month.

### 3. AI-governance evidence operations

- Target: 50–500-person B2B SaaS companies selling to European or enterprise buyers.
- Offer: assessment and maintained evidence room; legal conclusions stay with counsel/auditors.
- Test corpus: real vendor lists, policies, evaluation records, and security questionnaires.
- Pass gates: 2 paid assessments at $5k+; one vCISO/auditor/channel partner; at least 70% of recurring evidence gathered automatically with citations; no critical control marked complete without human approval.
- Kill/pivot: sales require unsupported certification claims, or customers treat the work as a one-off template purchase.

### 4. Atlassian compliance app

- Target: one compliance/change-control workflow inside Jira/Confluence.
- Offer test before build: clickable workflow demo and paid design-partner agreement.
- Pass gates: 20 interviews; 5 design partners; 3 written purchase commitments at $250+/month; repeated request for the same evidence export; install-to-value under 15 minutes.
- Kill/pivot: interest centers on generic summarization, or willingness to pay stays below $50/month.

## Reproducibility

- [`run_business_models.py`](run_business_models.py) contains the complete deterministic simulation.
- [`simulation_assumptions.json`](simulation_assumptions.json) contains every input range.
- [`simulation_summary.csv`](simulation_summary.csv) and [`sensitivity_summary.csv`](sensitivity_summary.csv) contain the generated outputs.
- Seed: `20261105`; Monte Carlo runs: `100,000`.

The next update should replace assumed validation, close, churn, price, and delivery-capacity distributions with observed data from the first 30 conversations and three paid pilots.
