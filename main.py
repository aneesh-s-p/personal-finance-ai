from input_handler import get_user_input
from logic import estimate_monthly_essentials, evaluate_priority
from ai_layer import ai_priority
from forecast import forecast_risk

print("=== Priority-Aware Explainable AI Money Manager ===")

# ------------------ INPUT ------------------

data = get_user_input()

monthly_essentials, estimate_source = estimate_monthly_essentials(
    data["income"], data["essential_expenses"]
)

emergency_months = data["emergency_fund"] / monthly_essentials

print(f"\nEmergency expense estimate source: {estimate_source}")

# ------------------ EMERGENCY STATUS ------------------

if emergency_months < 1:
    emergency_status = "CRITICAL (Less than 1 month coverage)"
elif emergency_months < 3:
    emergency_status = "BELOW MINIMUM (Below 3 months safety)"
elif emergency_months < 6:
    emergency_status = "YELLOW (Moderate safety)"
else:
    emergency_status = "GREEN (Strong safety buffer)"

# ------------------ AI PRIORITY ------------------

category, score, reasons, breakdown = ai_priority(
    data["expense_type"],
    data["commitment"],
    data["is_work_related"],
    data["no_alternative"],
)

# ------------------ EMI RATIO CHECK ------------------

emi_ratio = data["fixed_commitments"] / data["income"]

if emi_ratio >= 0.4:
    reasons.append("Fixed commitments exceed 40% of income (high financial stress)")
elif emi_ratio >= 0.3:
    reasons.append("Fixed commitments exceed 30% of income (moderate financial stress)")

# ------------------ FINAL DECISION ------------------

decision = evaluate_priority(emergency_months, category)

# ------------------ SUMMARY OUTPUT ------------------

print("\n================= DECISION SUMMARY =================")

print(f"\nExpense Category: {category}")
print(f"Commitment Level: {data['commitment']}")
print(f"Expense Amount: ₹{int(data['expense_amount'])}")

print("\nEmergency Fund Analysis:")
print(f"- Coverage: {round(emergency_months, 2)} months")
print(f"- Status: {emergency_status}")

print("\nPriority Score Breakdown:")
for k, v in breakdown.items():
    print(f"- {k}: {v}")
print(f"Final Score: {score}")

print("\nAI Reasoning Factors:")
if reasons:
    for r in reasons:
        print("-", r)
else:
    print("- No major financial risk signals detected.")

print(f"\nFinal Decision: {decision}")

# ------------------ FORECASTING ------------------

forecast = forecast_risk(
    data["income"],
    data["emergency_fund"],
    monthly_essentials,
    data["expense_amount"],
    data["fixed_commitments"],
)

print("\n================= FUTURE RISK FORECAST =================")

if emergency_months < 1:
    print("Emergency fund is critically underfunded.")
elif emergency_months < 3:
    print("Emergency fund is below minimum safety threshold.")
elif forecast["risk_months"] == 0:
    print("This expense would immediately push you into financial risk.")
elif forecast["risk_months"] is not None:
    print(f"Risk may occur in approximately {forecast['risk_months']} months.")
else:
    print("No immediate financial risk detected under current conditions.")

# ------------------ SPENDING GUIDANCE ------------------

monthly_surplus = data["income"] - monthly_essentials - data["fixed_commitments"]

print("\n================= SPENDING GUIDANCE =================")

print(f"- Monthly surplus available: ₹{int(monthly_surplus)}")
print(f"- To stay STABLE, keep discretionary spending below ₹{forecast['stable_limit']}.")
print(f"- To GROW your emergency fund, keep spending below ₹{forecast['growth_limit']}.")

if data["expense_amount"] >= monthly_surplus:
    print(
        "- This expense equals or exceeds your available surplus, "
        "leaving no safety margin."
    )

# ------------------ WHAT-IF SIMULATION ------------------

simulate = input("\nWould you like to simulate a different amount? (yes/no): ").lower()

if simulate == "yes":
    new_amount = float(input("Enter new expense amount: "))

    sim_forecast = forecast_risk(
        data["income"],
        data["emergency_fund"],
        monthly_essentials,
        new_amount,
        data["fixed_commitments"],
    )

    print("\n================= SIMULATION RESULT =================")

    if new_amount < data["expense_amount"]:
        print("- This reduces financial strain compared to the original amount.")
    elif new_amount > data["expense_amount"]:
        print("- This increases financial strain compared to the original amount.")

    if emergency_months < 1:
        print("Emergency fund remains critically underfunded.")
    elif emergency_months < 3:
        print("Emergency fund remains below safe threshold.")
    elif sim_forecast["risk_months"] == 0:
        print("This amount would push you into financial risk.")
    elif sim_forecast["risk_months"] is not None:
        print(f"Risk may occur in approximately {sim_forecast['risk_months']} months.")
    else:
        print("No immediate financial risk under this simulated amount.")
