# Hubitat-Events
Package for getting events from your Hubitat

[Hubitat](https://hubitat.com/) is a home automation hub. This repository helps you retrieve events from the hub.

## Requirements

1. A hubitat hub device.
2. The [Maker API](https://docs.hubitat.com/index.php?title=Maker_API) installed and enabled on one or more devices.
3. After you set up the Maker API, you should have:
   1. url for your devices
   2. token to connect

## How To

### How To Run

```
HUBITAT_TOKEN=<your-token> \
  HUBITAT_DEVICES_URL=http://hubitat.local/apps/api/<your-device-id>/devices \
  python3.9 src/hubitat.events.py
```

where you'd replace your token and device id with something like:

```
HUBITAT_TOKEN=abcde-911-zyx \
  HUBITAT_DEVICES_URL=http://hubitat.local/apps/api/12345/devices \
  python3.9 src/hubitat.events.py
```

### How to publish to python package index

```
make publish-pypi-test
```

To avoid having to type your username/password or token every time, save your token to a file `.pypirc`. Do not add this file to git.

### How to install the published version from pip

Create a virtual environment.

```
python3.9 -m venv .venv
. .venv/bin/activate
```

Then install from test pypi.
```
python3.9 -m pip install --index-url https://test.pypi.org/simple/ --no-deps hubitat-events-dhan
```

When you are done, close and clean up virtual environment.
```
deactivate
rm -rf .venv
```
