def next_state(current):
    flow = {
        "Hire": "Onboarding",
        "Onboarding": "Payroll",
        "Payroll": "Performance",
        "Performance": "Promotion",
        "Promotion": "Retirement"
    }

    return flow.get(current, "End")