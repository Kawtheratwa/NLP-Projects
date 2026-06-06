# PPU Chatbot

## Description

An AI assistant for **Palestine Polytechnic University (PPU)** students. Users can register, verify their email, and interact with a chatbot designed to answer university questions. The system supports uploading official documents so answers can be grounded in real university content using **RAG** (Retrieval-Augmented Generation).

## Features

- User registration with email verification
- JWT authentication and secure login
- Data models for chat messages and documents
- CORS support for the frontend (Vite/React)
- Architecture ready for RAG and intelligent responses

## Tech Stack

- **Backend:** FastAPI · SQLAlchemy · Alembic · Pydantic
- **Auth:** JWT · OAuth2
- **Database:** PostgreSQL (or SQLite for development)
- **Migrations:** Alembic

## Status

| Component | Status |
|-----------|--------|
| Authentication & database | ✅ Ready |
| Document upload & RAG | 🔄 In progress |
| Chat interface | 🔄 In progress |

## Run

```bash
pip install fastapi uvicorn sqlalchemy alembic python-jose passlib
uvicorn app.main:app --reload
```

API docs: `http://localhost:8000/docs`
