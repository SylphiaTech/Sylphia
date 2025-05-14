import statistics

def calculate_bot_score(trades):
    if not trades:
        return 0.0
    avg = sum(trades) / len(trades)
    stddev = statistics.stdev(trades) if len(trades) > 1 else 0
    score = (stddev / avg) * 100 if avg else 0
    return round(score, 2)

def classify_bot(score):
    if score > 80:
        return "High Risk Bot"
    elif score > 40:
        return "Moderate Risk"
    return "Low Risk Bot"

def detect_bot_clusters(trade_data):
    clusters = {}
    for trader, txs in trade_data.items():
        score = calculate_bot_score(txs)
        clusters[trader] = classify_bot(score)
    return clusters