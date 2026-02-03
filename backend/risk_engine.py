RISK_KEYWORDS = {
    "High": [
        "sole discretion",
        "without cause",
        "penalty",
        "indemnify",
        "non-compete",
        "unilateral",
        "terminate immediately"
    ],
    "Medium": [
        "may terminate",
        "subject to",
        "at any time",
        "reasonable notice"
    ]
}


def assess_risk(clause_text):
    text = clause_text.lower()

    for risk_level, keywords in RISK_KEYWORDS.items():
        for word in keywords:
            if word in text:
                return risk_level

    return "Low"
