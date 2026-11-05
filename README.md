# Family Command Center

A lightweight, self-hosted family dashboard built with Python and FastAPI, designed to run 24/7 on a wall-mounted 2-in-1 touchscreen Chromebook. It centralizes your household calendar feeds and shared task/grocery lists into a single, clean dark-mode interface.

## Features:
- Live calendar sync : Pulls upcoming events directly from private Apple/iCloud '.ics' calendar feeds.
- Task & Shopping Lists : Integrates with task APIs or local lists to keep household to-do visible.
- Auto-Refreshing Kiosk Display : Automatically reloads every 60 seconds (or programmable) to stay up to date without manual interaction.
- Dark-Mode Wall UI : Optimised for low-power, 24/7 display visibility.

## Tech Stack:
- Backend : Python 3.10+, FastAPI, Uvicorn
- Templating : Jinja2, HTML5, CSS Grid/Flexbox
- Data Integration : 'icalendar' (for '.ics' parsing), 'requests' (for external APIs), 'python-dotenv'


## Getting Started locally:
### 1. Clone the repository
```bash
git clone https://github.com/perpetualcoffee/family_command_center.git
cd family_command_center
```

### 2. Set up a virtual environment (recommended)
```bash
python -m venv venv
# On Windows:
venv/Scripts/activate
#On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requriements.txt
```

### 4. Configure Environment Variables
Copy the example environment file and add your private calendar or API URLs:
```bash
cp .vnv.example .env
```
open .env and fill in your private .ics feed URL.

### 5. Run the server
```bash
uvicorn main: app --reload --port 8000
```
Open your browser and navigate to http://localhost:8000.
