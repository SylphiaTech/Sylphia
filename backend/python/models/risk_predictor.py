def calculate_risk_score(metrics):
    weights = {
        "bot": 0.25,
        "sybil": 0.2,
        "whale": 0.15,
        "flashloan": 0.2,
        "sentiment": 0.2
    }
    total = 0
    for key, value in metrics.items():
        score = value if isinstance(value, (int, float)) else 0
        total += weights.get(key, 0) * score
    return round(min(total, 100), 2)