from src.constants import get_hubitat_token


def test_hubitat_token_default():
    # GIVEN no environment variables set

    # WHEN token is fetched
    test_token = get_hubitat_token()

    # THEN the test token should match the default value
    assert test_token == "Dummy token. Set real one with environment variable"
