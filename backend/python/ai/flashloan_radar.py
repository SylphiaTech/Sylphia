def simulate_flashloan_trace(transactions):
    loaned = sum(tx["amount"] for tx in transactions if tx["type"] == "loan")
    repaid = sum(tx["amount"] for tx in transactions if tx["type"] == "repay")
    return {"loaned": loaned, "repaid": repaid, "net": loaned - repaid}

def evaluate_flashloan_risk(trace):
    if trace["net"] > 0:
        return "Risky: Loan not fully repaid"
    if trace["loaned"] > 1_000_000 and trace["repaid"] == trace["loaned"]:
        return "Suspicious Flashloan Pattern"
    return "Normal"