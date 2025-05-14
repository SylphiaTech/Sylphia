def track_whale_volume_movement(volumes):
    gradient = [volumes[i+1] - volumes[i] for i in range(len(volumes)-1)]
    trends = []
    for g in gradient:
        if g > 10000:
            trends.append("surge")
        elif g < -10000:
            trends.append("dump")
        else:
            trends.append("stable")
    return trends

def summarize_whale_behavior(trends):
    counts = {"surge": 0, "dump": 0, "stable": 0}
    for t in trends:
        counts[t] += 1
    return counts