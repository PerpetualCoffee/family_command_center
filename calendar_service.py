# Fetching the .ics feed, parsing events, date math, cachine

# from config import settings

def get_upcoming_events():
    #parsing logic
    return [{"title": "Dentist", "time": "14:00"}]

# This lets me test just the calendar logic by running:
# python calendar_service.py
if __name__ == "__main__":
    events = get_upcoming_events()
    print("Fetched events:", events)