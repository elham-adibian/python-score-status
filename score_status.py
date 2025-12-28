def score_status(score):
    if score < 0 or score > 100:
        return "invalid"
    elif score < 50:
        return "fail"
    elif score < 75:
        return "pass"
    elif score < 90:
        return "good"
    else:
        return "excellent"


scores = [45, -3, 60, 78, 92, 50, 120]
results = []

for score in scores:
    results.append(score_status(score))

print(results)
