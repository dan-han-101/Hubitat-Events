# Hubitat-Events
Package for fetching events from your Hubitat.

[Hubitat](https://hubitat.com/) is a home automation hub. This repository helps you retrieve events from the hub.

## Requirements

1. A hubitat hub device.
2. The [Maker API](https://docs.hubitat.com/index.php?title=Maker_API) installed and enabled on one or more devices.
3. After you set up the Maker API, you should have:
   1. url for your devices
   2. token to connect

## How To

### How to run and test with Docker (using local source files)

```
docker build -f local.Dockerfile -t test.local.hubitat-events .

# Run hubitat_events command
docker run --rm test.local.hubitat-events

# Or open shell to run and test
docker run -it --rm test.local.hubitat-events sh
```

### How to run and test with Docker (using pypi package)

```
docker build -f pypi.Dockerfile -t test.pypi.hubitat-events .

# Run hubitat_events command
docker run --rm test.pypi.hubitat-events

# Or open shell to run and test
docker run -it --rm test.pypi.hubitat-events sh
```

### How to run and test with virtual environment

Create a virtual environment.

```
python3.9 -m venv .venv
. .venv/bin/activate
```

Build and install from the local source tree.
```
pip install .
```

Run
```
HUBITAT_TOKEN=<your-token> \
  HUBITAT_DEVICES_URL=http://hubitat.local/apps/api/<your-device-id>/devices \
  .venv/bin/hubitat_events
```

where you'd replace your token and device id with something like:

```
HUBITAT_TOKEN=abcde-911-zyx \
  HUBITAT_DEVICES_URL=http://hubitat.local/apps/api/12345/devices \
  .venv/bin/hubitat_events
```

When you are done, close and clean up virtual environment.
```
deactivate
rm -rf .venv
```

### How to publish to python package index

```
make publish-pypi-test
```

To avoid having to type your username/password or token every time, save your token to a file `$HOME/.pypirc`. Do not add this file to git.

You can then install the package

```
pip install --index-url https://test.pypi.org/simple/ hubitat-events-dhan
```
