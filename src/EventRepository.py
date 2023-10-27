from .Event import Event

class EventRepository:
    def __init__(self) -> None:
        self.group_id = None
        
    def load_last_event(self, group_id) -> Event:
        pass