from .EventRepository import EventRepository
from .Event import Event

class EventRepositorySpy(EventRepository):
    def __init__(self) -> None:
        super().__init__()
        self.output = None
        
    def load_last_event(self, group_id) -> Event:
        return self.output