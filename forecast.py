def forecast_risk(
    income,
    emergency_fund,
    monthly_essentials,
    discretionary_amount,
    fixed_commitments,
    min_safe_months=3,
):
    base_surplus = income - monthly_essentials - fixed_commitments

    min_safe_amount = monthly_essentials * min_safe_months

    if emergency_fund <= min_safe_amount:
        risk_months = 0
    else:
        net_change = base_surplus - discretionary_amount
        if net_change >= 0:
            risk_months = None
        else:
            risk_months = (emergency_fund - min_safe_amount) / abs(net_change)

    stable_limit = max(0, base_surplus)
    growth_limit = max(0, base_surplus * 0.5)

    return {
        "risk_months": None if risk_months is None else round(risk_months, 2),
        "stable_limit": int(stable_limit),
        "growth_limit": int(growth_limit),
    }
