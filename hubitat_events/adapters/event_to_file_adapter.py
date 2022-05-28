from datetime import datetime


class DeviceWriter:
    def __init__(self, filename: str = "./output/devices.txt"):
        self.filename = filename

    def save_device(
        self, device_id: int, device_type: str, device_name: str, device_label: str
    ):

        with open(self.filename, "a") as devices:
            devices.write(f"{device_id},{device_type},{device_name},{device_label}\n")
        return True


class EventWriter:
    def __init__(self, filename: str = "./output/events.txt"):
        self.filename = filename

    def save_event(self, device_id: int, event_date: datetime, event_value: float):

        with open(self.filename, "a") as output:
            output.write(f"{device_id},{event_date},{event_value}\n")
        return True
