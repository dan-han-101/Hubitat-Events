from datetime import datetime
from sqlalchemy import create_engine

db_name = "hubitat_events_db"  # database"
db_user = "hubitat_events_user"
db_password = "hubitat_events_password"
db_host = "db"
db_port = "5432"

# Connect to the database
db_string = "postgresql://{}:{}@{}:{}/{}".format(
    db_user, db_password, db_host, db_port, db_name
)
db = create_engine(db_string)


class DeviceWriter:
    def __init__(self, filename: str = "./output/devices.txt"):
        self.filename = filename

    def save_device(
        self, device_id: int, device_type: str, device_name: str, device_label: str
    ):

        db.execute(
            "INSERT INTO devices (device_id, device_type, device_name, device_label)"
            + " VALUES (%(device_id)s, %(device_type)s, %(device_name)s, %(device_label)s)"
            + " ON CONFLICT(device_id) DO UPDATE SET(device_type, device_name, device_label) ="
            + " (EXCLUDED.device_type, EXCLUDED.device_name, EXCLUDED.device_label)",
            {
                "device_id": device_id,
                "device_type": device_type,
                "device_name": device_name,
                "device_label": device_label,
            },
        )
        return True


class EventWriter:
    def __init__(self):
        pass

    def save_event(self, device_id: int, event_date: str, event_value: float):

        # Convert string to a timestamp object
        event_timestamp = datetime.strptime(event_date, "%Y-%m-%dT%H:%M:%S%z")

        # Convert switches to numeric values
        if event_value == "off":
            event_value = 0
        if event_value == "on":
            event_value = 1
        event_value = float(event_value)

        # Upsert event data
        db.execute(
            "INSERT INTO events (device_id, event_timestamp, event_value)"
            + " VALUES (%(device_id)s, %(event_timestamp)s, %(event_value)s)"
            + " ON CONFLICT(device_id, event_timestamp)"
            + " DO UPDATE SET event_value = EXCLUDED.event_value",
            {
                "device_id": device_id,
                "event_timestamp": event_timestamp,
                "event_value": event_value,
            },
        )

        return True
