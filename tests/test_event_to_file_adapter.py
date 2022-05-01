from datetime import datetime
from hubitat_events.adapters.event_to_file_adapter import EventWriter


def test_event_to_file_smoke_test():
    # GIVEN
    test_id = 1
    test_date = datetime.now()
    test_value = 2
    ew = EventWriter()

    # WHEN
    response = ew.save_event(test_id, test_date, test_value)

    # THEN
    assert response