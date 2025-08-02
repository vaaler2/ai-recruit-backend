def evaluate_applicant(data):
    # Tally JSON-ből kinyert válaszok
    name = data.get("Name")
    age = data.get("Age")
    experience = data.get("Experience")
    motivation = data.get("Motivation")

    score = 0

    if experience and int(experience) > 2:
        score += 1
    if motivation and len(motivation) > 50:
        score += 1
    if age and 18 <= int(age) <= 40:
        score += 1

    decision = "Alkalmas" if score >= 2 else "Nem alkalmas"

    return {
        "név": name,
        "pont": score,
        "döntés": decision
    }
