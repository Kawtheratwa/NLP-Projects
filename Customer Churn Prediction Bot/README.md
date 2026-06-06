# Customer Churn Prediction Bot

## Description

An Arabic web chatbot that estimates **customer churn** — the likelihood that a customer will leave a company. It collects data through an interactive conversation (age, income, years with the company, number of products, credit score, and support calls), then returns an instant prediction: **Stay ✅** or **Leave ❌**.

## Features

- Arabic chatbot UI
- Step-by-step data collection through interactive questions
- Real-time prediction using Logistic Regression
- Simple, responsive design

## Tech Stack

- **Backend:** Python · Flask
- **ML:** scikit-learn (Logistic Regression) · pandas
- **Frontend:** HTML · CSS · JavaScript

## Run

```bash
pip install flask pandas scikit-learn
python app.py
```

Then open `http://localhost:5000` in your browser.
