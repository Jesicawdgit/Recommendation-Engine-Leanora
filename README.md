Understood — clean, professional, no unnecessary emojis.
Here is a polished, interview-ready and GitHub-ready README for Learnora.

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

The user enters a learning question, for example:
“How do I learn Machine Learning?”

The frontend (React) sends the query to the Flask backend through a REST API.

---

### 2. Semantic Encoding

The backend uses a fine-tuned SentenceTransformer model (`learnora_finetuned_stv2`) to convert the query into a high-dimensional vector embedding.

This embedding represents the semantic meaning of the text rather than matching keywords.

---

### 3. Vector Similarity Search (FAISS)

All 16,000+ learning resources are pre-encoded into embeddings and stored in a FAISS vector index.

The query embedding is compared against the indexed resource embeddings using cosine similarity.
FAISS retrieves the top-k most semantically similar resources in milliseconds.

---

### 4. Metadata Retrieval and Filtering

Each resource contains structured metadata including:

* Title
* Summary
* Labels (topics)
* Difficulty level
* Prerequisites
* Credibility score
* Content type (video/article)

The backend filters and ranks the retrieved resources based on:

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

The roadmap is generated in real time based on the user’s query.

---

### 6. Frontend Rendering

The structured roadmap is returned as JSON and rendered in a React-based chat interface.

Users can:

* View structured learning paths
* Explore categorized resources
* Click resources directly
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

* `learnora_metadata_final.json` (structured resource dataset)
* `learnora_faiss_final.index` (vector index for fast similarity search)

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
* Chat-style user interaction

---

## Challenges Faced

1. Training and Scaling Embeddings
   Initially, OpenAI embeddings were used but proved expensive and insufficient for large-scale metadata processing.
   The solution was to fine-tune a SentenceTransformer model locally, which improved semantic consistency and reduced cost.

2. Large Dataset Processing
   Encoding and indexing 16,000+ resources required batch processing and optimized FAISS indexing.

3. Structuring Generated Roadmaps
   Ensuring correct ordering based on prerequisites and difficulty required additional metadata-based logic.

---

## Summary

Learnora combines semantic search, vector similarity indexing, and metadata-driven generation to create personalized learning roadmaps. It bridges the gap between raw educational content and structured learning guidance by dynamically generating learning paths tailored to each user query.

---

If you would like, I can also provide:

* A shorter version for public GitHub
* A resume-ready 4–5 line project description
* A technical architecture diagram version for documentation
