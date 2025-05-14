def validate_token_input(data: dict) -> bool:
    return (
        isinstance(data, dict)
        and "address" in data
        and isinstance(data["address"], str)
        and len(data["address"]) > 20
    )

def validate_transaction(tx: dict) -> bool:
    required_keys = {"amount", "type", "timestamp"}
    return required_keys.issubset(tx.keys())