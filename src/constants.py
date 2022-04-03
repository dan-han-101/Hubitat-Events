import os

def get_hubitat_token():
    return os.getenv(
        "HUBITAT_TOKEN", "Dummy token. Set real one with environment variable"
    )
