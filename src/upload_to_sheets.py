import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json

# Define the scope and authenticate using your JSON credentials file
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("ielts-progress-integration-1d399a2e5517.json", scope)
client = gspread.authorize(creds)

# Open the Google Sheet (make sure the sheet is shared with your service account)
# Using the new title "IELTS Score"
sheet = client.open("IELTS Score").sheet1

def load_progress():
    try:
        # Open the updated data file name
        with open("score.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def upload_progress_to_sheets():
    progress = load_progress()
    # Clear existing data and set headers
    sheet.clear()
    headers = ["Date", "Score", "Detailed", "Study Hours"]
    sheet.append_row(headers)

    for entry in progress:
        # Prepare the row with the detailed field included
        row = [
            entry.get("date"),
            entry.get("score"),
            entry.get("detailed"),
            entry.get("study_hours")
        ]
        sheet.append_row(row)
    print("Progress data uploaded to Google Sheets successfully.")

if __name__ == "__main__":
    upload_progress_to_sheets()
