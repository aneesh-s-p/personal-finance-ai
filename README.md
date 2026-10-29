# Personal Finance AI: Priority-Aware Explainable Money Manager

A command-line tool that tells you whether a planned purchase is **ALLOW**, **WARN** or **BLOCK**, and explains why in plain language. It looks at your emergency fund, fixed commitments and how essential the purchase is, rather than only checking whether you can afford it.

## How it works
1. **Inputs:** monthly income, emergency savings, fixed commitments (EMIs, rent), optional essential expenses, and details of the purchase (type, amount, commitment level, work-related, alternatives).
2. **Emergency-fund coverage:** months of essential expenses covered, with tiers (critical under 1 month, below minimum under 3, moderate under 6, strong 6+).
3. **Priority score:** weighs the expense type (NEED, DESIRE, WANT), long-term commitment, work relevance and cheaper alternatives (`ai_layer.py`).
4. **Decision rules:** `logic.py` blocks spending when coverage is under 1 month, warns under 3 months, and allows only essential needs once the fund is healthy.
5. **Risk forecast:** estimates how many months until the emergency fund drops below the 3-month minimum if the spending repeats (`forecast.py`), plus stable and growth spending limits.
6. **Explanation and what-if:** prints the reasoning (`explain.py`) and lets you test a different amount.

## Files
| File | Purpose |
|---|---|
| `main.py` | Runs the interactive tool |
| `input_handler.py` | Collects and validates user input |
| `logic.py` | Essentials estimate and ALLOW/WARN/BLOCK rules |
| `ai_layer.py` | Priority scoring and reasoning factors |
| `forecast.py` | Risk-months forecast and spending limits |
| `explain.py` | Plain-language explanation |
| `experiment.py` | Compares the rules with two budgeting baselines on simulated households |
| `behavior.py`, `estimator.py`, `learning.py` | Experimental modules (spending log, behaviour-based essentials estimate, simple learning score); not yet connected to `main.py` |

## Run it
```
python main.py          # interactive decision tool
python experiment.py    # simulation of 1,000 households
```
Python 3.8 or newer, no extra packages needed.

## Experiment
`experiment.py` generates 1,000 random households and compares three rules: a surplus rule, the 50/30/20 rule, and this model. It counts approvals and how many were "risky" (made when the emergency fund covered under 3 months).

Because this model is designed never to approve spending when the fund is under 3 months, its risky-approval count is zero by construction. The experiment therefore shows how much stricter the model is (it approves far fewer purchases), not that it is more accurate. Validating it would need real household outcomes.

## Limitations
- Rule-based, not a trained model, and the experiment uses synthetic data.
- Thresholds (1, 3 and 6 months) follow common personal-finance guidance and are not personalised.
- Not financial advice.
