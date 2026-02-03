def explain_clause_simple(clause_text, risk_level):
    """
    Dummy LLM explanation (API-free).
    Used for hackathon demo without external API calls.
    """

    explanation = [
        f"This clause has a {risk_level.lower()} level of risk.",
        "It defines obligations that may impact the business.",
        "You should review this clause carefully before signing."
    ]

    return "\n".join(f"- {line}" for line in explanation)
