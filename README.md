🤖 Moodle Bot - Automated Check-in / Check-out
This bot automates your daily Moodle attendance for BeCode using playwright.
It automatically performs check-ins and check-outs on a fixed daily schedule (e.g., 8:55 AM, 12:30 PM, 1:25 PM, 5:00 PM), and can run on GitHub Actions — so it works even if your computer is off.

📌 Features
✅ Automatically logs in to Moodle

🕗 Performs check-in and check-out at scheduled times

🌐 Runs automatically every weekday via GitHub Actions

💬 Sends notifications to Discord after each check-in/out

🔐 Keeps your credentials safe using environment variables

---

🧠 How it works
The main_scheduler.py script checks the local time (Europe/Brussels) and triggers the following actions:


| Time       | Action         |
|------------|----------------|
| 08:55 AM   | Check-in       |
| 12:30 PM   | Check-out      |
| 01:25 PM   | Check-in       |
| 05:00 PM   | Final check-out|

---

## 🚀 Setup Locally

1. Clone the project

```bash
git clone https://github.com/Manziherve/BeCode-Thomas5-Moodle_bot.git
cd BeCode-Thomas5-Moodle_bot


2. Create and fill your .env file


⚠️❗⚠️  Never share this file or upload it to GitHub! ⚠️❗⚠️

MOODLE_USERNAME=your.username
MOODLE_PASSWORD=your.password
ICAL_URL=https://your-ical-url.ics
MOODLE_BOT_NOTIFICATIONS=https://discord.com/api/webhooks/XXXX/XXXX

⚠️❗⚠️  Never share this file or upload it to GitHub! ⚠️❗⚠️

3. Install dependencies

pip install -r requirements.txt
playwright install chromium

⚙️ Setup GitHub Actions (Automatic Run)

1. Push your project to GitHub
Make sure your full project is uploaded except the .env file.

2. Add your secrets to GitHub
Go to:

Repo → Settings → Secrets and Variables → Actions → New Repository Secret
Add:

MOODLE_USERNAME

MOODLE_PASSWORD

MOODLE_BOT_NOTIFICATIONS

3. GitHub Actions Workflow
Ensure this file exists:

.github/workflows/moodle_automation.yml
Use this content:

name: Moodle Daily Automation

on:
  schedule:
    # Weekdays (Mon–Fri)
    - cron: '55 8 * * 1-5'    # ⏰ 08:55 Check-in
    - cron: '30 12 * * 1-5'   # 🕧 12:30 Check-out
    - cron: '25 13 * * 1-5'   # 🕜 13:25 Check-in
    - cron: '0 17 * * 1-5'    # 🕔 17:00 Final check-out
  workflow_dispatch:         # ✅ Manual run option

jobs:
  moodle:
    runs-on: ubuntu-latest
    steps:
      - name: 📥 Clone repo
        uses: actions/checkout@v3

      - name: 🐍 Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: 📦 Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
          playwright install

      - name: ✅ Run full day automation
        env:
          MOODLE_USERNAME: ${{ secrets.MOODLE_USERNAME }}
          MOODLE_PASSWORD: ${{ secrets.MOODLE_PASSWORD }}
          MOODLE_BOT_NOTIFICATIONS: ${{ secrets.MOODLE_BOT_NOTIFICATIONS }}
        run: python main_full_day.py
After pushing, go to the "Actions" tab in GitHub to see it run.

✅ Discord Notifications
After each check-in or check-out, the bot sends a message like:

✅ Check-in complete (athome) at 08:55
🏁 Check-out complete at 17:00
❌ Check-in failed: error logs...
🧪 Test Locally
You can simulate any action manually:

python checkin.py athome
python checkin.py atcampus
python checkout.py


## 🗂️ Project Structure

moodle-bot/
├── .github/
│ └── workflows/
│ └── moodle_automation.yml 🧠 GitHub Actions workflow (scheduled)
├── main_scheduler.py 🚀 Main script – decides when to check in/out
├── checkin.py ✅ Script for check-in
├── checkout.py 🔴 Script for check-out
├── requirements.txt 📦 Python dependencies
├── .env 🔐 Environment variables (excluded from Git)


📦 requirements.txt

ics==0.7.1
requests
playwright
python-dotenv


❤️ Credits

Built with ❤️ by Hervé M. just to make your daily routine easier and less stressful ❤️

Happy automating! If you need help, ping me on Discord or GitHub!

Enjoy.

---
for the Discord Notifications (MOODLE_BOT_NOTIFICATIONS) contact me ...
Let me know if you want it exported as a downloadable file or you want to tweak tone/style.
