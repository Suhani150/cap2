# AI-Powered Desktop Voice Assistant using NLP, DistilBERT, LangChain and FastAPI

## Abstract
The AI-Powered Desktop Voice Assistant is a smart desktop automation system developed using Python and FastAPI. The project integrates Natural Language Processing (NLP), transformer-based intent classification, and retrieval-based query handling to process user commands intelligently.

The assistant performs tasks such as opening applications, handling automation commands, processing search queries, and retrieving information using LangChain and FAISS vector search. The system uses DistilBERT for intent classification, spaCy for entity extraction, and FastAPI for backend API integration.

This project demonstrates the practical integration of machine learning, NLP pipelines, vector databases, and backend systems to build a modular AI-powered assistant.

---

# Objectives

- To develop an AI-powered desktop assistant capable of understanding natural language commands.
- To implement NLP preprocessing and entity extraction techniques.
- To integrate DistilBERT for intent classification.
- To implement semantic query retrieval using LangChain and FAISS.
- To build a modular FastAPI-based backend architecture.
- To automate desktop-related tasks through Python.

---

# Key Features

- NLP-based command processing
- Regex-based text preprocessing
- Entity extraction using spaCy
- DistilBERT-based intent classification
- LangChain + FAISS retrieval pipeline
- HuggingFace embeddings integration
- Desktop automation execution
- FastAPI backend API
- Command chaining support
- Structured JSON responses

---

# Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| FastAPI | Backend API framework |
| spaCy | Entity extraction |
| Transformers | DistilBERT integration |
| DistilBERT | Intent classification |
| LangChain | Retrieval pipeline |
| FAISS | Vector database |
| HuggingFace Embeddings | Semantic embeddings |
| Regex (`re`) | Text preprocessing |
| Git & GitHub | Version control |

---

# System Workflow

```text
User Input
    ↓
Preprocessing & Cleaning
    ↓
Entity Extraction
    ↓
DistilBERT Intent Classification
    ↓
Command Routing
    ↓
Automation / Query Retrieval
    ↓
JSON Response Output
```

---

# Project Architecture

## 1. Preprocessing Module
The preprocessing module cleans and normalizes user input using:
- lowercase conversion
- whitespace removal
- regex-based cleaning

---

## 2. Entity Extraction Module
The entity extraction module identifies useful entities such as:
- application names
- browser names
- search queries

spaCy and rule-based keyword matching were used for entity extraction.

---

## 3. Intent Classification Module
DistilBERT transformer model was integrated for intent classification.

The module classifies user commands into:
- automation
- query

---

## 4. LangChain + FAISS Retrieval Module
LangChain and FAISS were implemented to perform semantic similarity search using embeddings.

Workflow:
- text chunking
- embedding generation
- vector storage
- similarity retrieval

---

## 5. Automation Execution Module
The executor module performs automation tasks such as:
- opening Chrome
- opening Notepad
- opening Calculator
- opening File Explorer
- taking screenshots
- showing desktop

---

## 6. FastAPI Backend Integration
FastAPI was used to expose API endpoints for communication between frontend, backend, and ML modules.

---

# Folder Structure

```bash
AI-Voice-Assistant/
│
├── ml/
│   ├── preprocess.py
│   ├── entities.py
│   ├── input_pipeline.py
│   ├── distilbert_intent.py
│   ├── langchainrag.py
│   ├── executor.py
│   ├── main_pipeline.py
│
├── app.py
├── README.md
├── requirements.txt
```

---

# Installation Guide

## Step 1 — Clone Repository

```bash
git clone <repository-url>
cd AI-Voice-Assistant
```

---

## Step 2 — Create Virtual Environment

```bash
python -m venv venv
```

---

## Step 3 — Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

---

## Step 4 — Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Project

## Start FastAPI Server

```bash
uvicorn app:app --reload
```

---

# API Endpoint

## POST `/process-command`

### Example Request

```json
{
  "text": "open chrome and what is AI"
}
```

---

# Example Functionalities

| Command | Action |
|---|---|
| open chrome | Opens Chrome browser |
| open notepad | Opens Notepad |
| open calculator | Opens Calculator |
| open explorer | Opens File Explorer |
| take screenshot | Opens screenshot tool |
| show desktop | Minimizes all windows |
| what is AI | Semantic query retrieval |

---

# Team Contributions

## Subrat Ranjan
- DistilBERT integration
- LangChain + FAISS implementation
- FastAPI integration
- Automation execution
- ML pipeline orchestration
- API response handling

## Suhani
- NLP preprocessing
- Entity extraction
- Input pipeline development
- Data structuring
- NLP workflow support

---

# Challenges Faced

- Integrating transformer models in low-resource environments
- Managing dependency conflicts
- Handling command chaining
- Implementing semantic retrieval
- Structuring modular ML architecture

---

# Future Improvements

- Voice input support
- Speech-to-text integration
- Text-to-speech responses
- Advanced fine-tuned transformer models
- Multi-language support
- Cloud deployment
- GUI/Desktop application integration

---

# Conclusion

The AI-Powered Desktop Voice Assistant successfully integrates NLP preprocessing, transformer-based intent classification, semantic retrieval systems, and desktop automation into a unified modular architecture.

The project demonstrates practical implementation of:
- Natural Language Processing
- DistilBERT transformers
- LangChain retrieval systems
- FAISS vector databases
- FastAPI backend APIs
- Automation execution pipelines

This project provided valuable experience in AI system integration, backend development, modular software architecture, and machine learning workflow implementation.
