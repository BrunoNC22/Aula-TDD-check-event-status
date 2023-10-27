from src.EventRepositorySpy import EventRepositorySpy
from src.Event import Event
from src.CheckLastEventStatus import CheckLastEventStatus
from datetime import datetime, timedelta

def test_get_last_event_data():
    """
    It should get last event data
    """
    load_last_event_repository = EventRepositorySpy()
    check_last_event_status = CheckLastEventStatus(load_last_event_repository)
    
    check_last_event_status.perform('group_id')
    
    assert load_last_event_repository.group_id == 'group_id'
    assert check_last_event_status.calls_count == 1
    
def test_check_status_done_when_group_has_no_event():
    """
    It should return status done when group has no event
    """
    load_last_event_repository = EventRepositorySpy()
    load_last_event_repository.output = None
    check_last_event_status = CheckLastEventStatus(load_last_event_repository)
    
    result = check_last_event_status.perform('group_id') 
    
    assert result == 'done'

def test_check_status_active_when_group_event_is_not_done():
    """
    It should return status active when group event is not done
    """
    load_last_event_repository = EventRepositorySpy()
    actual_date = datetime.now()
    start_date = actual_date - timedelta(hours=1)
    end_date = actual_date + timedelta(hours=1)
    load_last_event_repository.output = Event(start_date=start_date, end_date=end_date)
    check_last_event_status = CheckLastEventStatus(load_last_event_repository)
    
    result = check_last_event_status.perform('group_id')
    
    assert result == 'active'

def test_check_status_active_when_datetime_is_equal_event_end_date():
    """
    It should return status active when datetime is equal event end date
    """
    load_last_event_repository = EventRepositorySpy()
    actual_date = datetime.now()
    start_date = actual_date - timedelta(hours=1)
    end_date = actual_date
    load_last_event_repository.output = Event(start_date=start_date, end_date=end_date)
    check_last_event_status = CheckLastEventStatus(load_last_event_repository)
    
    result = check_last_event_status.perform('group_id')
    
    assert result == 'active'
    
def test_check_status_done_when_event_and_note_market_are_closed():
    """
    It should return status done when event and note market are closed
    """
    load_last_event_repository = EventRepositorySpy()
    actual_date = datetime.now()
    start_date = actual_date - timedelta(hours=2)
    end_date = actual_date - timedelta(hours=1, minutes=5)
    load_last_event_repository.output = Event(start_date=start_date, end_date=end_date)
    check_last_event_status = CheckLastEventStatus(load_last_event_repository)
    
    result = check_last_event_status.perform('group_id')
    
    assert result == 'done' 
    
def test_check_status_in_review_when_the_event_is_over_but_is_within_the_note_market_period():
    """
    It should return status in review when the event is over, but is within the note market period.
    """
    load_last_event_repository = EventRepositorySpy()
    actual_date = datetime.now()
    start_date = actual_date - timedelta(hours=2)
    end_date = actual_date - timedelta(minutes=30)
    load_last_event_repository.output = Event(start_date=start_date, end_date=end_date)
    check_last_event_status = CheckLastEventStatus(load_last_event_repository)
    
    result = check_last_event_status.perform('group_id')
    
    assert result == 'in review' 
