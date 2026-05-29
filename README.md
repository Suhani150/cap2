# AI-Powered Desktop Voice Assistant using NLP, DistilBERT, LangChain, FAISS and FastAPI

## Abstract
The AI-Powered Desktop Voice Assistant is an intelligent desktop automation and query-handling system developed using Python and FastAPI. The project integrates Natural Language Processing (NLP), transformer-based intent classification, semantic retrieval systems, and desktop automation to process user commands intelligently.

The assistant can understand natural language commands, classify user intent, extract entities, execute desktop automation tasks, and retrieve semantically relevant information using vector-based similarity search.

The system uses:
- DistilBERT for intent classification
- spaCy for entity extraction
- LangChain and FAISS for semantic retrieval
- HuggingFace embeddings for vector generation
- FastAPI for backend API integration

This project demonstrates the practical implementation of modern AI technologies, machine learning pipelines, vector databases, and modular backend integration in a real-world desktop assistant application.

---

# Objectives

- To develop an AI-powered desktop assistant capable of understanding natural language commands.
- To implement NLP preprocessing and entity extraction techniques.
- To integrate transformer-based intent classification using DistilBERT.
- To implement semantic query retrieval using LangChain and FAISS.
- To build a modular FastAPI backend architecture.
- To automate desktop-level operations using Python.
- To demonstrate integration between AI modules and backend systems.

---

# Key Features

- NLP-based command processing
- Regex-based text preprocessing
- Entity extraction using spaCy
- DistilBERT-based intent classification
- LangChain + FAISS semantic retrieval
- HuggingFace embeddings integration
- Dynamic desktop automation execution
- Intelligent YouTube and Google search support
- Dynamic app detection and opening
- FastAPI REST API integration
- Command chaining support
- Structured JSON responses
- Modular ML pipeline architecture

---

# Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| FastAPI | Backend API framework |
| spaCy | NLP entity extraction |
| Transformers | Transformer model integration |
| DistilBERT | Intent classification |
| LangChain | Semantic retrieval pipeline |
| FAISS | Vector database |
| HuggingFace Embeddings | Embedding generation |
| Regex (`re`) | Text preprocessing |
| Git & GitHub | Version control |
| OS & Webbrowser Modules | Desktop automation |

---

# System Workflow

```text
User Input
      ↓
FastAPI Backend
      ↓
Text Preprocessing
      ↓
Entity Extraction
      ↓
Intent Classification
      ↓
Command Routing
      ↓
Automation Execution OR Semantic Retrieval
      ↓
JSON Response Output
```

---

# Project Architecture

## 1. Preprocessing Module
The preprocessing module cleans and normalizes raw user input using:
- lowercase conversion
- whitespace removal
- regex-based text cleaning

This improves NLP consistency and model performance.

---

## 2. Entity Extraction Module
The entity extraction module identifies important entities such as:
- application names
- browser names
- automation keywords
- search queries

spaCy NLP processing and rule-based keyword matching were used for extraction.

---

## 3. Intent Classification Module
DistilBERT transformer model was integrated for intent classification.

The module classifies user commands into:
- automation
- web_search
- query

A hybrid intent-routing approach was implemented using rule-based NLP logic for improved real-time command reliability.

---

## 4. LangChain + FAISS Retrieval Module
LangChain and FAISS were implemented to perform semantic similarity search using vector embeddings.

### Workflow:
- text chunking
- embedding generation
- vector storage
- similarity search
- relevant answer retrieval

This module enables semantic understanding of user queries.

---

## 5. Automation Execution Module
The executor module performs intelligent desktop automation tasks such as:
- opening Chrome
- opening Notepad
- opening Calculator
- opening File Explorer
- opening VS Code
- opening Paint
- opening Spotify
- opening YouTube
- taking screenshots
- showing desktop
- battery status retrieval

The system supports dynamic application opening using NLP-based entity extraction and OS-level command execution.

Example:
- open chrome
- open spotify
- launch telegram
- search coldplay songs on YouTube

Automation is executed using Python OS commands and web browser integration.

---

## 6. FastAPI Backend Integration
FastAPI was used to expose REST API endpoints for communication between:
- frontend
- backend
- machine learning modules

The API processes user commands and returns structured JSON responses.

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
├── assistant.py
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

## Run Interactive Assistant

```bash
python assistant.py
```

---

# API Endpoint

## POST `/process-command`

### Example Request

```json
{
  "text": "open chrome and what is artificial intelligence"
}
```

---

# Example Functionalities

| Command | Action |
|---|---|
| open chrome | Opens Chrome browser |
| open spotify | Opens Spotify |
| open vscode | Opens VS Code |
| open paint | Opens Paint |
| open youtube | Opens YouTube |
| search Coldplay songs on youtube | Searches YouTube dynamically |
| search artificial intelligence | Searches Google |
| take screenshot | Opens screenshot tool |
| show desktop | Minimizes all windows |
| show battery | Displays battery percentage |

---

# Sample JSON Response

```json
{
  "ml_output": [
    {
      "clean_text": "open chrome",
      "entities": {
        "app": "chrome"
      },
      "intent": "automation"
    }
  ],
  "actions": [
    {
      "status": "Opened Chrome"
    }
  ]
}
```

---

# Interactive Assistant Support

The project includes an interactive terminal-based AI assistant that continuously accepts user commands and processes them through the NLP pipeline.

Example:

```text
Enter command: search coldplay songs on youtube

Classified Intent: web_search

Extracted Entities:
{
  "platform": "youtube",
  "query": "coldplay songs"
}

Action Result:
{
  "status": "Searching 'coldplay songs' on YouTube"
}
```

The assistant supports:
- dynamic automation
- intelligent web search
- command chaining
- structured NLP outputs

---

# Team Contributions

## Subrat Ranjan
- DistilBERT integration
- LangChain + FAISS implementation
- FastAPI integration
- Automation execution
- ML pipeline orchestration
- API response handling
- Semantic retrieval integration

## Suhani Ranjan
- NLP preprocessing
- Entity extraction
- Input pipeline development
- Data structuring
- NLP workflow support
- Command processing support

---

# Challenges Faced

- Integrating transformer models in low-resource environments
- Managing dependency conflicts
- Implementing semantic retrieval systems
- Handling command chaining
- Structuring modular ML architecture
- Integrating ML modules with backend APIs

---

# Future Improvements

- Voice input support
- Speech-to-text integration
- Text-to-speech responses
- Advanced transformer fine-tuning
- Multi-language support
- Cloud deployment
- GUI/Desktop application integration
- Real-time conversational memory
- Mobile application integration

---

# Conclusion

The AI-Powered Desktop Voice Assistant successfully integrates NLP preprocessing, transformer-based intent classification, semantic retrieval systems, and desktop automation into a unified modular architecture.

The project demonstrates practical implementation of:
- Natural Language Processing
- DistilBERT transformer models
- LangChain retrieval pipelines
- FAISS vector databases
- HuggingFace embeddings
- FastAPI backend APIs
- Desktop automation execution

The assistant also supports dynamic application automation and intelligent platform-aware web search using NLP-based entity extraction.

This project provided valuable experience in:
- AI system integration
- backend development
- modular software architecture
- machine learning workflows
- semantic retrieval systems
- API integration and automation

The system represents a scalable foundation for future intelligent assistant applications.
