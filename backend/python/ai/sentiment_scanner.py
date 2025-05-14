from collections import Counter

def extract_keywords(tweets):
    keywords = []
    for t in tweets:
        for word in t.split():
            if len(word) > 3 and word.isalpha():
                keywords.append(word.lower())
    return Counter(keywords).most_common(10)

def evaluate_market_mood(keywords):
    mood_score = 0
    positive_keywords = {"moon", "bullish", "pump"}
    negative_keywords = {"rug", "bearish", "dump"}

    for word, freq in keywords:
        if word in positive_keywords:
            mood_score += freq
        elif word in negative_keywords:
            mood_score -= freq

    if mood_score > 5:
        return "Bullish"
    elif mood_score < -5:
        return "Bearish"
    return "Neutral"