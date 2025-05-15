import subprocess
import datetime
import os
import requests
from ics import Calendar
from dotenv import load_dotenv
from zoneinfo import ZoneInfo  # Python 3.9+

load_dotenv()

def get_location_from_ical():
    ical_url = os.getenv("ICAL_URL")
    if not ical_url:
        print("ICAL_URL is missing in your .env or GitHub secrets.")
        return None

    try:
        response = requests.get(ical_url)
        response.raise_for_status()
        calendar = Calendar(response.text)
        today = datetime.date.today()

        for event in calendar.events:
            if event.begin.date() == today:
                summary = event.name.strip().lower()
                if "on site" in summary:
                    return "atcampus"
                elif "at home" in summary:
                    return "athome"
        return None
    except Exception as e:
        print(f"Failed to fetch calendar: {e}")
        return None

def notify_discord(message):
    webhook_url = os.getenv("DISCORD_WEBHOOK")
    if webhook_url:
        try:
            requests.post(webhook_url, json={"content": message})
        except Exception as e:
            print(f"Failed to notify Discord: {e}")
    else:
        print("No DISCORD_WEBHOOK set in environment.")

def main():
    now = datetime.datetime.now(ZoneInfo("Europe/Brussels"))
    current_time = now.strftime("%H:%M")

    print(f"Running main_scheduler at {current_time}")

    if current_time in ["08:55", "13:25"]:
        location = get_location_from_ical()
        if location:
            print(f"Detected location: {location}")
            subprocess.run(["python", "checkin.py", location])
            notify_discord(f"Check-in for {location} done at {current_time}")
        else:
            print("No valid event found in iCal today.")
            notify_discord(f"No check-in — location not detected at {current_time}")

    elif current_time in ["12:30", "17:00"]:
        print("Performing check-out...")
        subprocess.run(["python", "checkout.py"])
        notify_discord(f"Check-out done at {current_time}")

    else:
        print("No scheduled action for this time.")

if __name__ == "__main__":
    main()
