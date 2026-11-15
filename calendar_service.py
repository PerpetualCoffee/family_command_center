# Fetching the .ics feed, parsing events, date math, cachine

import os
import json
from ics import Calendar
from config import settings
import requests
import arrow

CACHE_FILE = "cache.json"

def save_cache(events_data):
    # Handles writing the events to cache.json
    with open(CACHE_FILE, "w") as f:
        json.dump(events_data, f, indent=2, default=str)

def load_cache():
    # Handles reading from cache.json if it exists
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r") as f:
            return json.load(f)
    return []

def filter_and_sort_events(raw_events):
    now = arrow.now()
    upcoming = []

    for event in raw_events:
        # Keep events that haven't ended yet
        if event.end and event.end >= now:
            upcoming.append({
                "title": event.name,
                "start": event.begin.format("YYYY-MM-DD HH:mm"),
                "end": event.end.format("YYY-MM-DD HH:mm") if event.end else None,
                "raw_start": event.begin # Useful for sorting!
            })
    # Sort chronologically by start time
    upcoming.sort(key=lambda x: x["raw_start"])

    # Remove raw_start so final output is clean strings
    for item in upcoming:
        del item["raw_start"]

    # Optional: only keep the next 10 or 15 events so the screen isn't overwhelmed
    return upcoming[:10]        

def get_upcoming_events():
    # Coordinates fetching live data, falling back to cache, and returning the events

    try:
        # 1. Fetch the raw .ics text for the URL
        response = requests.get(settings.calendar_url, timeout=10)
        response.raise_for_status() # Raise an error if the download failed
        ics_text = response.text

        # 2 Pase the text into an ics Calendar object
        calendar = Calendar(ics_text)

        # 3 Extract the details into clean Python dictionaries
        clean_events = filter_and_sort_events(calendar.events)

        save_cache(clean_events)
        return clean_events

    except Exception as e:
        print(f"Warning: {e}. Loading cache...")
        return load_cache
    


if __name__ == "__main__":
    # Test it out!
    data = get_upcoming_events()
    print(f"Loaded {len(data)} events.")