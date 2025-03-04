# IELTS-Progress

A personal project to track and improve IELTS scores—from 6.5 to 7.5—using data visualization, goal reminders, and Google Sheets integration. This repository also includes additional study resources and tips for Reading, Listening, Writing, and Speaking in the `docs/` folder.

---

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
  - [1. Data Visualization](#1-data-visualization)
  - [2. Goal Reminders](#2-goal-reminders)
  - [3. Google Sheets Integration](#3-google-sheets-integration)
- [IELTS Tips & Resources](#ielts-tips--resources)
- [License](#license)
- [Contributing](#contributing)

---

## Overview

This repository helps you log, analyze, and improve your IELTS study progress. You can:

- Record test dates, scores, and study hours in a JSON file.
- Visualize your overall and detailed section scores over time.
- Receive daily reminders to stay on track with your study plan.
- Upload your data to Google Sheets for easy access and sharing.
- Explore curated tips and resources for Reading, Listening, Writing, and Speaking.

## Features

1. **Data Visualization**  
   - `plot_score.py` displays overall IELTS scores, detailed section scores (Listening, Reading, Writing, Speaking), and study hours over time.

2. **Goal Reminders**  
   - `reminder.py` sends a console-based reminder every day at a specified time (currently 7 PM).

3. **Google Sheets Integration**  
   - `upload_to_sheets.py` uses the Google Sheets API to upload your IELTS progress to an online spreadsheet.

4. **IELTS Study Resources**  
   - The `docs/` folder contains skill-specific tips and resources for Reading, Listening, Writing, and Speaking, plus a general `resources.md` for additional study materials.

---

## Project Structure

```plaintext
ielts-progress/
├── README.md                # Overview of your project
├── .gitignore               # Ignore files you don't want to commit
├── LICENSE                  # MIT License file
├── docs/                   # Documentation (IELTS tips & resources)
│   ├── reading.md          # IELTS Reading tips
│   ├── listening.md        # IELTS Listening tips
│   ├── writing.md          # IELTS Writing tips
│   ├── speaking.md         # IELTS Speaking tips
│   └── resources.md        # Additional resources (websites, books, etc.)
├── src/                    # Your source code (data visualization, Google Sheets integration)
│   ├── plot_score.py       # Data visualization script
│   └── upload_to_sheets.py # Google Sheets integration script
├── reminder.py             # Script for daily IELTS study reminders
└── score.json              # JSON file storing IELTS score data
```

### File Details

- **`.gitignore`**  
  Excludes common Python artifacts and your Google Sheets credentials file (e.g., `ielts-progress-integration-xxxx.json`).

- **`LICENSE`**  
  MIT License granting permission for anyone to use, modify, and distribute this project.

- **`reminder.py`**  
  Uses the `schedule` library to print a reminder message every day at 19:00 (7 PM).

- **`score.json`**  
  Stores your IELTS progress data in a JSON array of objects, each containing:
  ```json
  {
    "date": "YYYY-MM-DD",
    "score": float,
    "detailed": "L-x.x,R-x.x,W-x.x,S-x.x",
    "study_hours": float
  }
  ```

- **`src/plot_score.py`**  
  Reads `score.json` and plots three charts:
   - Overall IELTS Score vs. Date
   - Study Hours vs. Date
   - Detailed Scores (Listening, Reading, Writing, Speaking) vs. Date

- **`src/upload_to_sheets.py`**  
  Reads `score.json` and uploads your data to a Google Sheet titled **IELTS Score**.

- **`docs/ Folder`**  
  Contains detailed tips and resources for each IELTS skill area: 
   - **`reading.md, listening.md, writing.md, speaking.md`:** Skill-specific study guides and best practices.
   - **`resources.md`:** General resources such as official IELTS websites, recommended books, or practice platforms.

---

## Prerequisites

- **Python 3.7+**
  - Make sure you have Python installed. You can check your version with:
    ```bash
    python --version
    ```
- **Git (optional but recommended)**
  - Useful if you want to clone the repository instead of downloading a ZIP file.

### Python Libraries

- `matplotlib` for plotting
- `schedule` for reminders
- `gspread` and `oauth2client` for Google Sheets integration

### Google Cloud Setup (for Sheets Integration)

- A Google Cloud project with the Google Sheets API and Google Drive API enabled.
- A service account and its credentials file (e.g., `ielts-progress-integration-xxxx.json`).
- A Google Sheet shared with your service account email.

---

## Installation

1. **Clone or Download the Repository**  
   ```bash
   git clone https://github.com/YourUsername/IELTS-Progress.git
   cd IELTS-Progress
   ```

2. **(Optional) Create a Virtual Environment**
  ```bash
  python -m venv venv
  source venv/bin/activate  # On macOS/Linux
  venv\Scripts\activate     # On Windows```
  ```

3. **Install Dependencies**
If you have a requirements.txt, run:
   ```bash
   pip install -r requirements.txt
   ```
Otherwise, install them individually:
  ```bash
  pip install matplotlib schedule gspread oauth2client
  ```

4. **(Optional) Place Your Credentials File** 
If you plan to use Google Sheets integration, put your JSON credentials file (e.g., ielts-progress-integration-xxxx.json) in the project root.
Important: Keep this file out of version control for security (it’s already in .gitignore).

---

# Usage

## 1. Data Visualization

**Script:** `src/plot_score.py`

### How It Works:
- Reads `score.json` to get your IELTS data.
- Plots:
  - Overall Score vs. Date
  - Study Hours vs. Date
  - Detailed Scores (L, R, W, S) vs. Date

### How to Run:
```bash
python src/plot_score.py
```

## Tips

- Ensure `score.json` is in the root directory (the same level as `README.md`).
- Update or add new entries in `score.json` as you take more tests or study.

## 2. Goal Reminders

**Script:** `reminder.py`

### How It Works:
- Uses the `schedule` library to print a reminder every day at 19:00 (7 PM).

### How to Run:
```bash
python reminder.py
```
**Note:** Keep the script running in your terminal; it will print a message at the scheduled time.

## 3. Google Sheets Integration

**Script:** `src/upload_to_sheets.py`

### Prerequisites:
- Enable Google Sheets and Google Drive APIs in your Google Cloud project.
- Download your service account JSON (e.g., `ielts-progress-integration-xxxx.json`) and place it in the project root.
- Share your Google Sheet with the service account’s email.

### How to Run:
```bash
python src/upload_to_sheets.py
```

### What It Does:
- Reads data from `score.json`.
- Clears the existing data in your Google Sheet named "IELTS Score".
- Appends a header row, then adds each entry from `score.json` as a new row.

## IELTS Tips & Resources

This project also contains a `docs/` folder with various skill-specific guides and general resources:

- **Reading**
- **Listening**
- **Writing**
- **Speaking**
- **General Resources**

Feel free to explore these files for advice on improving each skill area, as well as recommended materials and websites to supplement your IELTS preparation.

---

## License

This project is licensed under the MIT License. You’re free to use, modify, and distribute this software under the terms of the license.

---

## Contributing

- Fork the repository.
- Create a new branch (e.g., `feature-improvement`).
- Commit your changes and push your branch.
- Open a Pull Request in this repository to discuss and merge your changes.

Feedback, suggestions, and contributions are welcome!
