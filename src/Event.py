from datetime import timedelta, datetime

class Event:
    def __init__(self, start_date:datetime, end_date:datetime) -> None:
        self.start_date = start_date
        self.end_date = end_date
        self.note_market = self.end_date + timedelta(hours=1)
        
    