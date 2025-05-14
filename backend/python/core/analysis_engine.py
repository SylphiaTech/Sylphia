from ai.bot_detector import calculate_bot_score, classify_bot
from ai.sybil_scanner import detect_sybil_wallets
from ai.whale_cluster import summarize_whale_behavior
from ai.flashloan_radar import evaluate_flashloan_risk
from ai.sentiment_scanner import evaluate_market_mood
from core.session_manager import Session

def run_analysis(input_data):
    session = Session()
    bot_score = calculate_bot_score(input_data["trades"])
    session.add_result("bot", classify_bot(bot_score))

    sybils = detect_sybil_wallets(input_data["wallets"])
    session.add_result("sybil", sybils)

    whale_trends = summarize_whale_behavior(input_data["whale_trends"])
    session.add_result("whale", whale_trends)

    flash_risk = evaluate_flashloan_risk(input_data["flash_trace"])
    session.add_result("flashloan", flash_risk)

    mood = evaluate_market_mood(input_data["keywords"])
    session.add_result("sentiment", mood)

    return session.get_summary()