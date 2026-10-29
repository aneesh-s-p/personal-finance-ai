def estimate_monthly_essentials(
    income,
    user_reported_essentials=None,
    log_file="expense_log.txt"
):
    """
    Hybrid estimator:
    1. Use user-reported essentials if provided
    2. Else estimate from logged NEED expenses
    3. Else fallback to 50% income heuristic
    """

    # 1️⃣ User-provided data (highest priority)
    if user_reported_essentials and user_reported_essentials > 0:
        return user_reported_essentials, "user_reported"

    # 2️⃣ Behavior-based estimation
    try:
        with open(log_file, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        lines = []

    need_total = 0
    need_count = 0

    for line in lines:
        _, category, amount = line.strip().split(",")
        if category == "NEED":
            need_total += float(amount)
            need_count += 1

    if need_count >= 3:  # minimum data threshold
        estimated = need_total / need_count
        return estimated, "behavior_based"

    # 3️⃣ Fallback heuristic
    return income * 0.5, "heuristic"
