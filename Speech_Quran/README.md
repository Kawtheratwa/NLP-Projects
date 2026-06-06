# Itqan

## Description

A web app that helps users **memorize the Quran** through voice recitation. The user selects a short surah, starts reciting via the microphone, and the system verifies each verse before moving to the next. When the surah is complete, the completion time is displayed.

## Features

- Selection of short surahs (Al-Kawthar, Al-Ikhlas, An-Nasr)
- Arabic recitation recognition via Web Speech API
- Verse-by-verse verification with encouraging feedback
- State machine to manage memorization sessions
- Fully Arabic RTL interface

## Tech Stack

- **Backend:** FastAPI
- **Frontend:** HTML · CSS · JavaScript · Jinja2 Templates
- **Speech:** Web Speech API (browser-based speech recognition)

## Run

```bash
pip install fastapi uvicorn jinja2
uvicorn app:app --reload
```

Then open `http://localhost:8000` in your browser.
