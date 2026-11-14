# main.py

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from calendar_service import get_upcoming_events


app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/")
def dashboard(request: Request):
    events = get_upcoming_events()
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"title": "Family Command Center", "events": events}
    )

"""
use requests once to download calendar feed and save it to a local test_calendar.ics file
   write parsing logic against the local file first; then change to the live version
   
   The local JSON Cache Pattern
   1. attempt fetch
   2. on success; parse the .ics, write the parsed events into cache.json and return the data
   3. on failure (e.g. RequestException or timeout): Catch the error, log a warning, load and return the contents of cache.json instead"""


# if __name__ == "__main__":
    # import uvicorn
    # uvicorn.run("main:app", host="0.0.0.0", port=8000, reload="True")