# AI Agent API Server (FastAPI + LangChain)
This project converts a LangChain-based AI agent into a production-ready REST API using FastAPI.  

The server exposes an endpoint that allows users to send prompts and receive AI-generated responses.

The system is designed to simulate real-world AI backend deployment workflows.

# Architecture

User
↓
FastAPI Endpoint
↓
LangChain Agent
↓
OpenAI Model
↓
Response

# Features

- REST API built with FastAPI
- LangChain integration
- Environment variable configuration
- Secure API key handling
- Ready for Docker deployment

- # Tech Stack
- Python
- FastAPI
- LangChain
- Uvicorn

### 1. Clone the repository
git clone https://github.com/Anasthedoc/mcp-api-server

### 2. Create virtual environment
python3 -m venv venv
source venv/bin/activate

### 3. Install dependencies
pip install -r requirements.txt

# Run the server
uvicorn app:app --reload
Then visit
http://localhost:8000/docs
