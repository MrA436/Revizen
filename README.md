# Revizen

> AI-powered exam survival intelligence for fast, high-yield revision.

Revizen is a PDF-based AI revision tool built using Python, Streamlit, OCR, and Groq API.

It extracts educational content from PDFs, processes it through an AI intelligence pipeline, and returns structured revision-focused outputs designed for stressed students and last-minute exam preparation.

Instead of generating large walls of notes, Revizen focuses on:

* rapid recall
* high-priority concepts
* exam-focused revision
* reduced cognitive overload

---

# Features

## Hybrid PDF Processing

Revizen supports both:

* standard text-based PDFs
* scanned/image-based PDFs

The extraction pipeline combines:

* `pypdf` for direct text extraction
* `EasyOCR` fallback for scanned pages

---

## AI-Powered Revision Intelligence

Revizen generates structured educational outputs including:

* High-priority revision notes
* Important exam questions
* Technical keywords
* Concise recall-oriented explanations

---

## Structured JSON Pipeline

The AI output is converted into structured JSON instead of raw markdown.

Example output structure:

```json id="gk3b0n"
{
  "high_priority_revision": [],
  "exam_questions": [],
  "keywords": []
}
```

This keeps the rendering cleaner and allows the intelligence layer to remain reusable across different interfaces.

---

## Cinematic Glassmorphism UI

The Streamlit frontend includes:

* dark cinematic styling
* glassmorphism panels
* progressive disclosure using expanders
* calmer revision flow
* structured visual hierarchy

---

## Downloadable Notes

Generated revision notes can be downloaded directly from the app.

---

# Tech Stack

## Backend & AI

* Python
* Groq API
* Structured JSON pipelines

## PDF & OCR

* pypdf
* EasyOCR
* pdf2image
* OpenCV

## Frontend

* Streamlit
* Custom CSS

---

# How Revizen Works

```text id="wnv4c8"
PDF Upload
↓
Text Extraction
↓
OCR Fallback (if needed)
↓
AI Prompt Processing
↓
Structured JSON Generation
↓
JSON Cleanup & Parsing
↓
Frontend Rendering
```

---

# Installation

Clone the repository:

```bash id="j6a4ec"
git clone https://github.com/MrA436/Revizen.git
cd Revizen
```

Install dependencies:

```bash id="2cuhje"
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file in the root directory:

```env id="5c9hlh"
GROQ_API_KEY=your_api_key_here
```

Get your API key from Groq Cloud.

---

# Run The Streamlit App

```bash id="o5sk91"
streamlit run app.py
```

---

# API Usage

Revizen also exposes its intelligence layer through FastAPI.

Run the API:

```bash id="3n58sv"
uvicorn api.main:app --reload
```

Example endpoint:

```text id="w7h8an"
POST /revision
```

Input:

```json id="n3ec2j"
{
  "text": "your extracted educational text here"
}
```

Output:

```json id="5fbc4g"
{
  "high_priority_revision": [],
  "exam_questions": [],
  "keywords": []
}
```

---

# Recommended PDF Guidelines

For best performance:

* Use PDFs under ~100 pages
* Clear scans/images work best
* English text recommended
* Avoid heavily corrupted scans

---

# Core Purpose

Revizen is designed to:

* reduce revision overwhelm
* improve scanability
* prioritize high-yield concepts
* help students revise faster under pressure

The focus is not generating more notes.

The focus is generating more useful revision.

---

# License

MIT License
