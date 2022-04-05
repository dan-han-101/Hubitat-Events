import os


def get_hubitat_base_url() -> str:
    return "http://hubitat.local/apps/api/391/devices"


def get_hubitat_token() -> str:
    return os.getenv(
        "HUBITAT_TOKEN", "Dummy token. Set real one with environment variable"
    )
