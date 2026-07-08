# HR AI Agent 🤖


## Overview

HR AI Agent is an AI powered chatbot that helps employees get answers related to HR processes like:

- Leave Management
- Payroll
- Job Creation
- Workforce Management


## Features

- AI powered HR chatbot
- Gemini API integration
- Knowledge base driven responses
- Intent detection
- REST API backend
- Responsive frontend UI


## Tech Stack

Backend:
- Python
- FastAPI
- Gemini AI
- Pydantic

Frontend:
- HTML
- CSS
- JavaScript

Tools:
- Git
- GitHub


## Architecture


User
 |
Frontend Chat UI
 |
FastAPI API
 |
Intent Detector
 |
Knowledge Base
 |
Gemini AI
 |
Response



## Setup


Clone repository

## git clone repo-url

## Create virtual environment

- python -m venv venv
- venv\Scripts\activate
- pip install -r requirements.txt
- uvicorn app.main:app --reload 

## Screenshots
### Chatbot UI

![Chatbot](screenshorts/chatbot.png)

### API Documentation

![Swagger](screenshorts/swagger.png)

AI Usage

Gemini AI was used for:

Natural language understanding
Generating HR responses
Context based answers using knowledge files

Knowledge files:

leave.json
jobs.json
payroll.json
workforce.json
Challenges
Designing intent detection
Integrating Gemini API
Connecting frontend with backend
Maintaining structured knowledge base
Future Improvements
Authentication
Employee database
Leave application workflow
Notifications
Admin dashboard


# Tech Stack


## Backend

- Python
- FastAPI
- Pydantic
- REST APIs


## AI

- Google Gemini API
- Prompt Engineering
- Intent Detection


## Frontend

- HTML
- CSS
- JavaScript


## Data

- JSON based knowledge repository



---

# Architecture


User

↓

Frontend Chat UI

↓

FastAPI Backend

↓

Intent Detection

↓

Knowledge Base Retrieval

↓

Gemini AI

↓

Response



---

# AI Usage


AI was used in the project for:

1. Response generation using Google Gemini API

2. Prompt engineering to control AI responses

3. Intent classification for HR queries

4. Designing chatbot workflow

5. Debugging and improving application structure using ChatGPT



---

# Assumptions


- HR policies are stored in structured JSON files.
- Employee specific data is not connected with database.
- Authentication is outside the project scope.
- Knowledge base can be extended with additional HR documents.
- Gemini responses are restricted using provided HR context.
