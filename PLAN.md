# Project Plan: Family_Command_Center (Python Edition)

A ~30-hour personal engineering project to build and deploy a centralised household dashboard on a local device.

---

## Core Development Phases (V1)

### Phase 1: Core FastAPI Server & Boilerplate (Hours 1–5)
* [ ] Initialize repository, `requirements.txt`, and virtual environment.
* [ ] Write a basic FastAPI app in `main.py` with a root `GET /` endpoint.
* [ ] Set up Jinja2 HTML templates and serve a static dark-mode dashboard card.
* **Verification:** Opening `http://localhost:8000` renders the styled template successfully.

### Phase 2: Calendar Feed Integration (Hours 6–15)
* [ ] Write a Python HTTP client function to fetch the `.ics` calendar feed URL securely from environment variables.
* [ ] Integrate an `.ics` parsing library to extract event titles, dates, and times.
* [ ] Pass parsed event data from Python into the Jinja2 HTML template.
* [ ] Offline JSON Caching: Fallback data storage so temporary Wi-Fi drops don't break the wall display.
* **Verification:** The dashboard dynamically displays upcoming Apple/iCloud events.

### Phase 3: Task & Grocery Integration & UI Polish (Hours 16–25)
* [ ] Integrate task or grocery list data (via Todoist API or local list logic).
* [ ] Refactor CSS layout into a split-screen dashboard (Schedule on left, Tasks/Groceries on right).
* [ ] Add a 60-second auto-refresh meta tag or client-side script for continuous wall display.
* **Verification:** Both calendar and grocery modules render side-by-side with zero manual refreshing.

### Phase 4: Packagin, Testing, and Deployment Readiness (Hours 26–30)
* [ ] Deploy the FastAPI app locally on your home network (or a lightweight cloud free-tier).
* [ ] Writing clear, step-by-step instructions in the README.md (cloning, .env setup, running with Uvicorn).
* [ ] Adding environment configuration handling (e.g. using pydantic-settings or python-dotenv).
* [ ] Writing unit tests for calendar-parsing and task logic.
* [ ] Setting up a simple script so the server launcehs automatically on boot.


---

## Version 2.0+ Future Roadmap

*Note: Future features will be modularised into separate Python packages to keep the core server clean.*

### Phase 1: Smart Home & Household Context (V2.1)
* [ ] **Local Weather & Rain Alerts:** Integrate OpenWeatherMap API with custom warning banners.
* [ ] **Automated Bin Night Tracker:** Date-logic module to display recycling/organics collection alerts.

### Phase 2: Advanced Meal Planning & Relational Lists (V2.2)
* [ ] **Weekly Meal Matrix:** Monday–Sunday dinner grid backed by a local JSON file.
* [ ] **One-Click Recipe-to-Shopping Conversion:** Automatically push recipe ingredients into the active grocery list.

### Phase 3: Gamified Chores & Family Inputs (V2.3)
* [ ] **Kid's Chore Tracker:** Interactive touch checkboxes mapped to individual family member profiles.
* [ ] **Digital Sticky Note Board:** A lightweight mobile form endpoint allowing family members to pin quick notes to the wall screen from their phones.

### Phase 4: Physical Mounting
* [ ] Configure device (i.e. Chromebook in Tablet Mode) with a full-screen browser pointing to the dashboard URL.
* [ ] Mount the device to the wall with a long USB-C power cable and secure housing.
* **Verification:** The wall-mounted touchscreen runs the app 24/7 without human intervention.
