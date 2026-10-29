import datetime

LOG_FILE = "expense_log.txt"

def log_expense(category, amount):
    date = datetime.date.today()
    with open(LOG_FILE, "a") as file:
        file.write(f"{date},{category},{amount}\n")
def analyze_patterns():
    try:
        with open(LOG_FILE, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        return []

    insights = []
    category_count = {}
    total_spent = 0

    for line in lines:
        _, category, amount = line.strip().split(",")
        amount = float(amount)
        total_spent += amount

        category_count[category] = category_count.get(category, 0) + 1

    for category, count in category_count.items():
        if count >= 3:
            insights.append(
                f"You frequently spend on {category} ({count} times recently)."
            )

    if total_spent > 0:
        insights.append(
            f"Total logged discretionary spending so far: ₹{int(total_spent)}"
        )

    return insights

def get_monthly_discretionary_average(log_file="expense_log.txt"):
    try:
        with open(log_file, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        return 0

    total = 0
    count = 0

    for line in lines:
        _, category, amount = line.strip().split(",")
        if category in ["DESIRE", "WANT"]:
            total += float(amount)
            count += 1

    if count == 0:
        return 0

    # Approximate monthly average
    return total / max(1, count / 4)

