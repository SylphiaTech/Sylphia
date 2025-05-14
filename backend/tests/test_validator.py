from backend.input_validator import validate_token_input

def test_valid_token():
    valid = {"address": "0xAABBCCDDEEFF112233445566778899"}
    assert validate_token_input(valid) is True

def test_invalid_token():
    invalid = {"address": ""}
    assert validate_token_input(invalid) is False