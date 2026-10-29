def get_user_input():
    income = float(input("Enter your monthly income: "))
    emergency_fund = float(input("Enter your current emergency savings: "))
    fixed_commitments = float(
        input("Enter total monthly fixed commitments (EMIs, rent, loans): ")
    )

    essential_expenses_input = input(
        "Enter your average monthly essential expenses (press Enter to skip): "
    )

    essential_expenses = (
        float(essential_expenses_input)
        if essential_expenses_input.strip() != ""
        else None
    )

    print("\nSelect expense type (important):")
    print("1 - NEED")
    print("    Essentials required for survival or basic functioning.")
    print("    Examples: food, rent, medicine, utilities")
    print("2 - DESIRE")
    print("    Comfort expenses that improve lifestyle but can be reduced.")
    print("    Examples: dining out, subscriptions, entertainment")
    print("3 - WANT")
    print("    Non-essential or luxury purchases, often high-cost.")
    print("    Examples: car upgrade, premium gadgets")

    expense_choice = input("Enter 1, 2, or 3: ")
    expense_type_map = {"1": "NEED", "2": "DESIRE", "3": "WANT"}
    expense_type = expense_type_map.get(expense_choice, "WANT")

    expense_amount = float(input("Enter the expense amount: "))

    print("\nSelect commitment level of this expense:")
    print("1 - LOW")
    print("    One-time, flexible, easy to stop.")
    print("2 - MEDIUM")
    print("    Recurring or habit-forming.")
    print("3 - HIGH")
    print("    Long-term obligation (EMI, contract, loan).")

    commitment_choice = input("Enter 1, 2, or 3: ")
    commitment_map = {"1": "LOW", "2": "MEDIUM", "3": "HIGH"}
    commitment = commitment_map.get(commitment_choice, "LOW")

    is_work_related = input(
        "Is this expense required for work or income generation? (yes/no): "
    ).lower()

    no_alternative = input(
        "Is there no cheaper alternative available? (yes/no): "
    ).lower()

    return {
        "income": income,
        "emergency_fund": emergency_fund,
        "fixed_commitments": fixed_commitments,
        "essential_expenses": essential_expenses,
        "expense_type": expense_type,
        "expense_amount": expense_amount,
        "commitment": commitment,
        "is_work_related": is_work_related,
        "no_alternative": no_alternative,
    }
