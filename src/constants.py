import os


def get_hubitat_devices_url() -> str:
    return os.getenv(
        "HUBITAT_DEVICES_URL",
        "http://hubitat.local/apps/api/12345/devices/Dummy URL."
        + " Set real one with an environment variable",
    )


def get_hubitat_token() -> str:
    return os.getenv(
        "HUBITAT_TOKEN", "Dummy token. Set real one with environment variable"
    )
