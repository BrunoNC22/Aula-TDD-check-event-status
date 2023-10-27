from .EventRepository import EventRepository
from datetime import datetime

class CheckLastEventStatus:
    def __init__(self, eventRepository: EventRepository) -> None:
        self.eventRepository = eventRepository
        self.calls_count = 0
    
    def perform(self, group_id: str) -> str:
        self.eventRepository.group_id = group_id
        self.calls_count += 1
        last_event = self.eventRepository.load_last_event(group_id)
        now = datetime.now()
        if last_event == None:
            return 'done'
        elif now > last_event.note_market:
            return 'done'
        elif last_event.end_date > now or last_event.end_date == now:
            return 'active'
        elif now > last_event.end_date and now < last_event.note_market:
            return 'in review'
        