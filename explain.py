def explain(decision, category, commitment, reasons, emergency_months):
    print("\nFinal Decision:", decision)

    # Human-friendly classification explanation
    print("\nHow this expense was understood:")
    print(f"- Expense type: {category}")

    if commitment == "1":
        print("- Commitment level: LOW (one-time, easy to stop)")
    elif commitment == "2":
        print("- Commitment level: MEDIUM (recurring or habit-forming)")
    else:
        print("- Commitment level: HIGH (long-term or EMI-based commitment)")

    print(
        f"- Emergency fund coverage: {emergency_months:.2f} months "
        f"(minimum safe: 3.00, recommended buffer: 3.50)"
    )

    # AI reasoning
    if reasons:
        print("\nAI Reasoning Factors:")
        for r in reasons:
            print("-", r)

    # Decision explanation
    print("\nWhy this decision was made:")

    if decision == "BLOCK":
        print(
            "This expense was blocked because it is non-essential, involves high financial risk, "
            "and your current emergency safety buffer is insufficient."
        )
        print("Suggestion: Strengthen your emergency fund before reconsidering this expense.")

    elif decision == "WARN":
        print(
            "This expense is allowed with caution. It may impact your financial safety "
            "if repeated or increased."
        )
        print("Suggestion: Consider delaying, reducing the amount, or finding alternatives.")

    else:
        print(
            "This expense fits within your current financial priorities and safety limits."
        )
        print("Suggestion: You may proceed, but continue monitoring your finances.")
