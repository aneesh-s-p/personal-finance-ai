def estimate_monthly_essentials(income, user_value):
    if user_value is not None:
        return user_value, "user_reported"
    # fallback heuristic
    return income * 0.5, "estimated_50_percent_rule"


def evaluate_priority(emergency_months, category):
    if emergency_months < 1:
        return "BLOCK"

    if emergency_months < 3:
        return "WARN"

    if category == "NEED":
        return "ALLOW"

    return "WARN"
