# main.py

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from calendar_service import get_upcoming_events


app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/")
def dashboard(request: Request):
    # 1. Call the function
    events_data = get_upcoming_events()

    # 2. Quick debug print to check what main.py actually sees
    print("--- DEBUG ---")
    print("Keys in schedule:", events_data.keys())
    print("Count in this_week:", len(events_data.get("this_week", [])))
    print("Count in later:", len(events_data.get("later", [])))
    print("-------------")

    # 3. Pass into context
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "title": "Family Command Center",
            "date_range": events_data.get("date_range", ""),
            "planning_events": events_data.get("planning_events", []),
            "this_week": events_data.get("this_week", []),
            "later": events_data.get("later", []),
        }
    )




# if __name__ == "__main__":
    # import uvicorn
    # uvicorn.run("main:app", host="0.0.0.0", port=8000, reload="True")