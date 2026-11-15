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

def categorise_events(raw_events):
    now = arrow.now()
    one_week_later = now.shift(days=+7)

    if now.format("MMMM") == one_week_later.format("MMMM"):
        date_range_str = f"{now.format('D')} - {one_week_later.format('D MMMM')}"
    else:
        date_range_str = f"{now.format('D MMM')} - {one_week_later.format('D MMMM')}"

    this_week = []
    upcoming_later = []
    planning_events = []

    for event in raw_events:
        # Keep events that haven't ended yet
        event_end = event.end or event.begin
        if event_end >= now:

            # Check for the special planning tag first!
            if event.description and "Planning" in event.description:
                days_until = (event.begin.date() - now.date()).days

                countdown_label = "Today!" if days_until == 0 else f"{days_until} days until"

                planning_events.append({
                    "title": event.name,
                    "countdown": countdown_label,
                    "start": event.begin.format("D MMMM YYYY"),
                    "raw_start": event.begin # Useful for sorting!
                })

            # Check if event falls within the next 7 days:
            elif event.begin <= one_week_later:
                # Friendly, day-focused format for this week: "Wednesday"
                this_week.append({
                    "title": event.name,
                    "start": event.begin.format("dddd [at] h:mm A"),
                    "end": event.end.format("h:mm A") if event.end else None,
                    "raw_start": event.begin # Useful for sorting!
                })
            
            else:
                # Date/Year-focused format for nearby future events: "15 April 2027"
                upcoming_later.append({
                    "title": event.name,
                    "start": event.begin.format("dddd D MMMM [at] h:mm A"),
                    "end": event.end.format("h:mm") if event.end else None,
                    "raw_start": event.begin # Useful for sorting!
                })

    # Sort chronologically by start time
    this_week.sort(key=lambda x: x["raw_start"])
    upcoming_later.sort(key=lambda x: x["raw_start"])

    # Remove raw_start so final output is clean strings
    for item in this_week:
        del item["raw_start"]
    for item in upcoming_later:
        del item["raw_start"]

    # Optional: only keep the next 10 or 15 events so the screen isn't overwhelmed
    return {
        "date_range": date_range_str, # For the dashboard
        "planning_events": planning_events, # Those long-term events requiring planning
        "this_week": this_week,
        "later": upcoming_later[:5], # Just the next few long-term items
    }     

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
        clean_events = categorise_events(calendar.events)

        save_cache(clean_events)
        return clean_events

    except Exception as e:
        print(f"Warning: {e}. Loading cache...")
        return load_cache
    


if __name__ == "__main__":
    # Test it out!
    data = get_upcoming_events()
    print(f"Loaded {len(data)} events.")