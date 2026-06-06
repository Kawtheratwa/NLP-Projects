from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine, Base
from . import models

# Create database tables
# Base.metadata.create_all(bind=engine) # We will use Alembic for migrations instead

app = FastAPI(
    title="PPU Chatbot API",
    description="Backend API for the PPU AI Chatbot",
    version="1.0.0"
)

# Configure CORS
origins = [
    "http://localhost:5173", # Vite default port
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from app.routers import auth

@app.get("/")
def read_root():
    return {"message": "Welcome to PPU Chatbot API"}

app.include_router(auth.router)

@app.get("/health")
def health_check():
    return {"status": "healthy"}
