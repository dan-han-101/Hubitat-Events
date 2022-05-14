FROM python:3.9-slim-buster

RUN python3.9 -m pip install --no-cache-dir \
    --index-url https://test.pypi.org/simple/ \
    hubitat-events-dhan

CMD ["/usr/local/bin/hubitat_events"]