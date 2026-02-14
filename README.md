---

# Learnora – AI-Powered Learning Assistant

Learnora is a semantic search–based AI learning assistant that generates personalized learning roadmaps using vector embeddings and metadata-driven structuring.

It helps users discover relevant learning resources and organizes them into structured, easy-to-follow learning paths.

---

## Problem Statement

Online learning platforms contain large volumes of content but lack structured personalization. Learners often:

* Spend excessive time searching for relevant resources
* Struggle to determine what to learn first
* Cannot clearly differentiate beginner and advanced content
* Lack a structured learning sequence

Learnora addresses this by understanding user intent semantically and generating structured, personalized learning roadmaps dynamically.

---

## How It Works

### 1. User Query

The user enters a learning question (for example: “How do I learn Machine Learning?”).

The React frontend sends this query to the Flask backend through a REST API.

---

### 2. Semantic Encoding

The backend uses a fine-tuned SentenceTransformer model (`learnora_finetuned_stv2`) to convert the query into a high-dimensional embedding vector.

This embedding captures semantic meaning rather than relying on keyword matching.

---

### 3. Vector Similarity Search (FAISS)

All 16,000+ learning resources are pre-encoded and stored in a FAISS index.

The query embedding is compared against indexed vectors using cosine similarity.
FAISS retrieves the top-k most semantically similar resources in milliseconds.

---

### 4. Metadata Retrieval and Filtering

Each resource includes structured metadata such as:

* Title
* Summary
* Labels (topics)
* Difficulty level
* Prerequisites
* Credibility score
* Content type (video/article)

The backend filters and ranks results based on:

* Difficulty progression (Beginner → Advanced)
* Credibility score
* Prerequisite alignment
* Content type grouping

---

### 5. Roadmap Generation

The backend dynamically generates:

* A step-based learning roadmap
* A fishbone-style visual roadmap
* Categorized branches (Articles vs Videos)
* Ordered progression based on prerequisites

Each roadmap is generated in real time based on the user’s query.

---

### 6. Frontend Rendering

The structured roadmap JSON is returned to the React frontend and rendered in a chat-style interface.

Users can:

* View structured learning paths
* Explore categorized resources
* Open links directly
* Track session history

---

## Tech Stack

### Machine Learning

* SentenceTransformers (fine-tuned embedding model)
* FAISS (vector similarity search)
* PyTorch
* Hugging Face Transformers

### Backend

* Flask (REST API)
* Python
* JSON-based metadata storage

### Frontend

* React
* React Router
* LocalStorage for session persistence

### Data Layer

* `backend/datasets/learnora_metadata_final.json`
* `backend/datasets/learnora_faiss_final.index`

---

## System Architecture

User → React Frontend → Flask API → SentenceTransformer → FAISS Index → Metadata Filtering → Roadmap Generation → JSON Response → React UI

---

## Key Features

* Semantic search (meaning-based retrieval)
* Vector similarity search using FAISS
* Personalized roadmap generation
* Fishbone-style visual learning paths
* Difficulty and prerequisite-based sequencing
* Chat-style interaction

---

## Challenges Faced

1. Training and scaling embeddings
   OpenAI embeddings were initially used but became expensive at scale.
   A locally fine-tuned SentenceTransformer improved semantic consistency and reduced recurring API costs.

2. Large dataset processing
   Encoding and indexing 16,000+ resources required batch processing and optimized FAISS indexing.

3. Roadmap structuring
   Ensuring correct ordering by prerequisites and difficulty required additional metadata-driven logic.

---

## Local Setup

### Prerequisites

* Python 3.10+
* Node.js 18+ and npm
* Git

---

### Clone Repository

```bash
git clone https://github.com/Jesicawdgit/Recommendation-Engine.git
cd Recommendation-Engine
```

---

### Environment Variables

Create local environment files (not committed to version control).

#### frontend/.env

```
REACT_APP_AUTH0_DOMAIN=your-auth0-domain.us.auth0.com
REACT_APP_AUTH0_CLIENT_ID=your_auth0_client_id
```

#### backend/.env (if required)

```
# OPENAI_API_KEY=your_openai_api_key
# FLASK_ENV=development
```

---

### Run Backend (Port 5001)

```bash
cd backend
python -m venv .venv
```

Activate virtual environment:

**Windows**

```bash
.venv\Scripts\activate
```

**macOS/Linux**

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start backend:

```bash
python app_alt_port.py
```

Health check:

```
http://localhost:5001/api/health
```

---

### Run Frontend

Open a new terminal:

```bash
cd frontend
npm install
npm run dev
```

If `npm run dev` is not defined:

```bash
npm start
```

---

### Run Order

1. Start backend (`python app_alt_port.py`)
2. Start frontend (`npm run dev` or `npm start`)

---

## Summary

Learnora combines semantic search, vector similarity indexing, and metadata-driven generation to create personalized learning roadmaps. It bridges raw educational content and structured learning guidance by dynamically generating learning paths tailored to user intent.

---

