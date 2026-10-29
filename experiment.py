import random
from forecast import forecast_risk
from logic import evaluate_priority

# -----------------------------
# Synthetic Data Generator
# -----------------------------

def generate_household():
    income = random.randint(20000, 100000)

    essentials_ratio = random.uniform(0.3, 0.6)
    essentials = income * essentials_ratio

    fixed_ratio = random.uniform(0.1, 0.6)
    fixed_commitments = income * fixed_ratio

    emergency_months = random.uniform(0, 12)
    emergency_fund = essentials * emergency_months

    expense_amount = random.uniform(500, income * 0.5)

    category = random.choice(["NEED", "DESIRE", "WANT"])

    return {
        "income": income,
        "essentials": essentials,
        "fixed_commitments": fixed_commitments,
        "emergency_fund": emergency_fund,
        "expense_amount": expense_amount,
        "category": category,
    }

# -----------------------------
# Baseline 1 — Surplus Rule
# -----------------------------

def baseline_surplus(h):
    surplus = h["income"] - h["essentials"] - h["fixed_commitments"]
    return "ALLOW" if h["expense_amount"] <= surplus else "BLOCK"

# -----------------------------
# Baseline 2 — 50/30/20 Rule
# -----------------------------

def baseline_503020(h):
    discretionary_limit = 0.3 * h["income"]
    return "ALLOW" if h["expense_amount"] <= discretionary_limit else "BLOCK"

# -----------------------------
# Proposed Model
# -----------------------------

def proposed_model(h):
    emergency_months = h["emergency_fund"] / h["essentials"]

    decision = evaluate_priority(emergency_months, h["category"])

    forecast = forecast_risk(
        h["income"],
        h["emergency_fund"],
        h["essentials"],
        h["expense_amount"],
        h["fixed_commitments"],
    )

    return decision, forecast

# -----------------------------
# Experiment Runner
# -----------------------------

def run_experiment(n=1000):

    surplus_risky = 0
    rule503020_risky = 0
    proposed_risky = 0

    surplus_allow = 0
    rule503020_allow = 0
    proposed_allow = 0

    for _ in range(n):

        h = generate_household()
        emergency_months = h["emergency_fund"] / h["essentials"]

        # Baseline 1
        decision1 = baseline_surplus(h)
        if decision1 == "ALLOW":
            surplus_allow += 1
            if emergency_months < 3:
                surplus_risky += 1

        # Baseline 2
        decision2 = baseline_503020(h)
        if decision2 == "ALLOW":
            rule503020_allow += 1
            if emergency_months < 3:
                rule503020_risky += 1

        # Proposed
        decision3, _ = proposed_model(h)
        if decision3 == "ALLOW":
            proposed_allow += 1
            if emergency_months < 3:
                proposed_risky += 1

    print("\n===== EXPERIMENT RESULTS =====")
    print(f"Total households tested: {n}\n")

    print("Approval Counts:")
    print(f"- Surplus Rule: {surplus_allow}")
    print(f"- 50/30/20 Rule: {rule503020_allow}")
    print(f"- Proposed Model: {proposed_allow}")

    print("\nRisky approvals (Emergency < 3 months):")
    print(f"- Surplus Rule: {surplus_risky}")
    print(f"- 50/30/20 Rule: {rule503020_risky}")
    print(f"- Proposed Model: {proposed_risky}")

    print("\nRisky Approval Rate:")
    print(f"- Surplus Rule: {round(surplus_risky / max(1, surplus_allow), 3)}")
    print(f"- 50/30/20 Rule: {round(rule503020_risky / max(1, rule503020_allow), 3)}")
    print(f"- Proposed Model: {round(proposed_risky / max(1, proposed_allow), 3)}")

# -----------------------------
# Run
# -----------------------------

if __name__ == "__main__":
    run_experiment(1000)
