from datetime import datetime


class EventWriter:
    def __init__(self, filename: str = "./output.txt"):
        self.filename = filename

    def save_event(self, device_id: int, event_date: datetime, event_value: float):

        with open(self.filename, "a") as output:
            output.write(f"{device_id},{event_date},{event_value}\n")
        return True
