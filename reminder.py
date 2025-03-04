import schedule
import time

def reminder():
    print("Reminder: It's time to study for IELTS! Don't forget to review your materials.")

# Schedule a reminder every day at 7 PM
schedule.every().day.at("19:00").do(reminder)

if __name__ == "__main__":
    print("Goal reminders are running. Press Ctrl+C to stop.")
    while True:
        schedule.run_pending()
        time.sleep(60)