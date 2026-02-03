import re

CLAUSE_KEYWORDS = {
    "Termination": ["terminate", "termination"],
    "Payment": ["payment", "fees", "salary", "compensation"],
    "Confidentiality": ["confidential", "nda", "non-disclosure"],
    "Indemnity": ["indemnity", "indemnify"],
    "Jurisdiction": ["jurisdiction", "governing law", "court"],
    "Non-Compete": ["non-compete", "restriction"],
}


def split_into_clauses(text):
    clauses = []
    raw_clauses = re.split(r"\n\s*\d+\.|\n\s*[A-Z][A-Za-z ]+:", text)

    for idx, clause in enumerate(raw_clauses):
        clause = clause.strip()
        if len(clause) < 40:
            continue

        clause_type = "General"
        for key, keywords in CLAUSE_KEYWORDS.items():
            for word in keywords:
                if word.lower() in clause.lower():
                    clause_type = key
                    break

        clauses.append({
            "id": idx + 1,
            "type": clause_type,
            "text": clause
        })

    return clauses
