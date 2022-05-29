
CREATE TABLE IF NOT EXISTS devices (
    device_id integer,
    device_type text,
    device_name text,
    device_label text,
    PRIMARY KEY(device_id)
);
CREATE TABLE IF NOT EXISTS events (
    device_id integer,
    event_timestamp timestamp,
    event_value real,
    PRIMARY KEY (device_id, event_timestamp),
    CONSTRAINT devices_fk FOREIGN KEY(device_id) REFERENCES devices(device_id)
);
