from src.constants import get_hubitat_devices_url
from src.constants import get_hubitat_token


def test_hubitat_base_url_default():
    # GIVEN no environment variables set

    # WHEN token is fetched
    test_devices_url = get_hubitat_devices_url()

    # THEN the test token should match the default value
    assert "Dummy URL" in test_devices_url


def test_hubitat_token_default():
    # GIVEN no environment variables set

    # WHEN token is fetched
    test_token = get_hubitat_token()

    # THEN the test token should match the default value
    assert test_token == "Dummy token. Set real one with environment variable"
