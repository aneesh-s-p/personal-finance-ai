def ai_priority(expense_type, commitment, is_work_related, no_alternative):
    reasons = []

    # Base category weights
    weights = {"NEED": 0.8, "DESIRE": 0.5, "WANT": 0.3}
    category_weight = weights.get(expense_type, 0.3)

    # Commitment penalty
    commitment_penalty_map = {"LOW": 0.0, "MEDIUM": -0.1, "HIGH": -0.2}
    commitment_penalty = commitment_penalty_map.get(commitment, 0.0)

    # Work support bonus
    work_bonus = 0.1 if is_work_related == "yes" else 0.0

    # Alternative penalty
    alternative_penalty = -0.05 if no_alternative == "no" else 0.0

    priority_score = category_weight + commitment_penalty + work_bonus + alternative_penalty

    if commitment == "HIGH":
        reasons.append("High long-term financial commitment")
    if is_work_related == "yes":
        reasons.append("Expense supports income or job stability")
    if no_alternative == "no":
        reasons.append("Cheaper alternatives are available")

    breakdown = {
        "category_weight": category_weight,
        "commitment_penalty": commitment_penalty,
        "work_bonus": work_bonus,
        "alternative_penalty": alternative_penalty,
    }

    return expense_type, round(priority_score, 2), reasons, breakdown
