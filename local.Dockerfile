FROM python:3.9-slim-buster

WORKDIR /app

COPY . /app

RUN mkdir -p output/postgresql/data output/grafana

RUN python3.9 -m pip install .

CMD ["/usr/local/bin/hubitat_events"]
