# checkout.py
import os
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv

load_dotenv()

def run(pw):
    username = os.getenv("MOODLE_USERNAME")
    password = os.getenv("MOODLE_PASSWORD")

    browser = pw.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()

    print("Step 1: Logging into Moodle...")
    page.goto("https://moodle.becode.org/login/index.php?loginredirect=1")
    page.wait_for_timeout(1000)
    page.get_by_role("textbox", name="Username").fill(username)
    page.wait_for_timeout(1000)
    page.get_by_role("textbox", name="Password").fill(password)
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="Log in").click()

    print("Step 2: Navigating to Attendance page...")
    page.wait_for_timeout(3000)
    page.get_by_role("menuitem", name="My courses").click()
    page.wait_for_timeout(1000)
    page.get_by_role("link", name="LGG-2025-03-Thomas", exact=True).click()
    page.wait_for_timeout(1000)
    page.get_by_label("Content").get_by_role("link", name="Attendance").click()
    page.wait_for_timeout(1000)
    page.get_by_role("link", name="Days").click()
    page.wait_for_timeout(1000)
    page.get_by_role("link", name="Check out").click()

    print("Step 3: Check-out complete.")
    page.close()
    browser.close()

if __name__ == "__main__":
    print("Starting check-out...")
    with sync_playwright() as pw:
        run(pw)
