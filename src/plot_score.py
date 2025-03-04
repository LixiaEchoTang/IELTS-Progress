import json
import matplotlib.pyplot as plt
from datetime import datetime

def load_score():
    try:
        with open("score.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def parse_detailed(detail_str):
    # Expecting a string in the format "L-7.0,R-7.0,W-6.0,S-6.5"
    details = {}
    for item in detail_str.split(","):
        key, value = item.split("-")
        details[key.strip()] = float(value.strip())
    return details

def plot_score():
    score_data = load_score()
    if not score_data:
        print("No score data found.")
        return

    # Convert date strings to datetime objects
    dates = [datetime.strptime(entry["date"], "%Y-%m-%d") for entry in score_data]
    scores = [entry["score"] for entry in score_data]
    study_hours = [entry["study_hours"] for entry in score_data]

    # Extract detailed scores if available
    listening, reading, writing, speaking = [], [], [], []
    for entry in score_data:
        if "detailed" in entry:
            details = parse_detailed(entry["detailed"])
            listening.append(details.get("L", None))
            reading.append(details.get("R", None))
            writing.append(details.get("W", None))
            speaking.append(details.get("S", None))
        else:
            listening.append(None)
            reading.append(None)
            writing.append(None)
            speaking.append(None)

    # Create subplots: Score, Study Hours, and Detailed Scores
    plt.figure(figsize=(18, 6))

    # Plot IELTS Scores
    plt.subplot(1, 3, 1)
    plt.plot(dates, scores, marker='o', label="Score")
    plt.xlabel("Date")
    plt.ylabel("IELTS Score")
    plt.title("IELTS Score Over Time")
    plt.xticks(rotation=45)
    plt.legend()

    # Plot Study Hours
    plt.subplot(1, 3, 2)
    plt.bar(dates, study_hours, width=0.5, color='skyblue', label="Study Hours")
    plt.xlabel("Date")
    plt.ylabel("Study Hours")
    plt.title("Study Hours Over Time")
    plt.xticks(rotation=45)
    plt.legend()

    # Plot Detailed Scores for Listening, Reading, Writing, and Speaking
    plt.subplot(1, 3, 3)
    plt.plot(dates, listening, marker='o', label="Listening")
    plt.plot(dates, reading, marker='o', label="Reading")
    plt.plot(dates, writing, marker='o', label="Writing")
    plt.plot(dates, speaking, marker='o', label="Speaking")
    plt.xlabel("Date")
    plt.ylabel("Score")
    plt.title("Detailed IELTS Scores Over Time")
    plt.xticks(rotation=45)
    plt.legend()

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_score()
