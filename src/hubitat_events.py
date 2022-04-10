#!/usr/local/bin/python3.9

import requests
from constants import get_hubitat_devices_url, get_hubitat_token


def get_all_devices():
    url = f"{get_hubitat_devices_url()}?access_token={get_hubitat_token()}"
    r = requests.get(url)
    if r.status_code == 200:
        print("get_all_devices succeeded")
        devices = r.json()
        return devices
    else:
        print(f"get_all_devices failed. status = {r.status_code}")
        return {}


def get_events_for_id(device_id: int):
    url = (
        f"{get_hubitat_devices_url()}/{device_id}/events?"
        + f"access_token={get_hubitat_token()}"
    )
    r = requests.get(url)
    if r.status_code == 200:
        print("get_events_for_id succeeded")
        return r.json()
    else:
        print(f"get_events_for_id failed. status = {r.status_code}")
        return {}


if __name__ == "__main__":
    devices = get_all_devices()
    for d in devices:
        print(
            f"Device name={d['name']},"
            + f" label={d['label']}, "
            + f"type={d['label']}"
        )
        events = get_events_for_id(d["id"])
        for e in events:
            print(f"date={e['date']}, value={e['value']} ")
