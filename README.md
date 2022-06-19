# Hubitat-Events
Package for fetching events from your Hubitat.

[Hubitat](https://hubitat.com/) is a home automation hub. This repository helps you retrieve events from the hub.

The key features of this package include:

- code to fetch data from your Hubitat connected devices
- postgresql database to save data
- grafana dashboards to view data

## Requirements

1. A hubitat hub device.
2. The [Maker API](https://docs.hubitat.com/index.php?title=Maker_API) installed and enabled on one or more devices.
3. After you set up the Maker API, you should have:
   1. url for your devices
   2. token to connect
4. Docker as the application runner

## How To

### How to fetch data

Run the following command with the variables replaced with real values.

```
HUBITAT_TOKEN=<your-token> \
  HUBITAT_DEVICES_URL=http://hubitat.local/apps/api/<your-device-id>/devices \
  docker compose run data-refresh
```

where you'd replace your token and device id with something like:

```
HUBITAT_TOKEN=abcde-911-zyx \
  HUBITAT_DEVICES_URL=http://hubitat.local/apps/api/12345/devices \
  .venv/bin/hubitat_events
```

If it worked, it will create:
- output/devices.txt - a list of hubitat devices
- output/events.txt - a dump of hubitat event information
- output/postgresql - postgres database data 

### How to view data in grafana
After you fetch data from your hubitat, you can view the saved data in grafana. Run

```
docker compose up grafana
```

After the container starts to run, go to [http://localhost:3000](http://localhost:3000). You should see the grafana login screen. You should be able to login with a user name of `admin` and a password of `admin`.

Go to [http://localhost:3000/datasources](http://localhost:3000/datasources). There should be one data source named "PostgreSql". Go into this data source and click on "Save & test" to confirm that everything is working.

Go to [http://localhost:3000/dashboards](http://localhost:3000/dashboards). There should be one dashboard named "All Hubitat Devices and Events Dashboard". This dashboard has data from all your hubitat devices. You should create new dashboards to create custom views of your data.

### How to publish to python package index

```
make publish-pypi-test
```

To avoid having to type your username/password or token every time, save your token to a file `$HOME/.pypirc`. Do not add this file to git.

You can then install the package

```
pip install --index-url https://test.pypi.org/simple/ hubitat-events-dhan
```
