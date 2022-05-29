#!/usr/local/bin/python3.9

import requests
from hubitat_events.util.constants import get_hubitat_devices_url, get_hubitat_token

# from hubitat_events.adapters.event_to_file_adapter import DeviceWriter
# from hubitat_events.adapters.event_to_file_adapter import EventWriter

from hubitat_events.adapters.event_to_db_adapter import DeviceWriter
from hubitat_events.adapters.event_to_db_adapter import EventWriter


def get_all_devices():
    url = f"{get_hubitat_devices_url()}?access_token={get_hubitat_token()}"
    print(f"get_all_devices from {url}")
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


def main():
    device_writer = DeviceWriter()
    event_writer = EventWriter()

    devices = get_all_devices()
    for d in devices:
        device_writer.save_device(d["id"], d["type"], d["name"], d["label"])
        print(
            f"Device id={d['id']},"
            + f" type={d['type']},"
            + f" name={d['name']},"
            + f" label={d['label']}"
        )
        events = get_events_for_id(d["id"])
        for e in events:
            event_writer.save_event(d["id"], e["date"], e["value"])


if __name__ == "__main__":
    main()
