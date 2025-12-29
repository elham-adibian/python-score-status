def loan_status(income, credit_score):
    """
    Determines loan approval status based on income and credit score.
    
    Parameters:
    income (numeric): Monthly income
    credit_score (numeric): Credit score (0–100)
    
    Returns:
    str: loan status
    """
    if income < 0 or credit_score < 0:
        return "invalid"
    elif income < 3 and credit_score < 50:
        return "rejected"
    elif income < 5 or credit_score < 70:
        return "review"
    else:
        return "approved"


cases = [
    (2, 40),
    (4, 60),
    (5, 75),
    (-1, 80),
    (6, 45)
]

results = []
for income, credit_score in cases:
    results.append(loan_status(income, credit_score))

print(results)
