# 🎬 FilmLab: ScriptWhisper - AI-Powered Screenwriting Assistant

**Status**: 🚧 In Development  
**Author**: Bhavya Samhitha Mallineni

## 🧠 About This Project

This project is part of **FilmLab**, an initiative to bridge the gap between artificial intelligence and storytelling. 

**ScriptWhisper** is an AI/NLP-based platform designed to help aspiring screenwriters—especially those without formal training—craft emotionally resonant, well-structured, and properly formatted screenplays.

The goal is to democratize storytelling by offering real-time feedback, emotional analysis, and AI-generated rewrite suggestions to improve the quality of any screenplay.

---

## 🎯 Problem Statement

Aspiring writers often have brilliant ideas but struggle with the technical aspects of screenwriting—such as structure, formatting, pacing, and emotional development. Without affordable access to professional guidance, many promising scripts go unrecognized.

---

## ✅ Solution Overview

ScriptWhisper acts as a virtual writing coach using NLP to:
- Detect and correct formatting errors
- Analyze emotional arcs across scenes
- Identify key story beats (setup, climax, resolution)
- Evaluate and rewrite character dialogues
- Educate users with examples and insights from real films

---

## 🚀 Key Features (Planned MVP)

- 📝 **Format Checker** – Validates scene headings, actions, dialogues
- 📊 **Emotional Arc Analyzer** – Visualizes emotional intensity page-by-page
- 🎭 **Story Structure Validator** – Detects act breaks and beat points
- 🗣️ **Dialogue Evaluator** – Scores tone and realism, with AI-powered rewrites
- 🧠 **Learning Layer** – Offers brief explanations and tips

---

## 🧪 Tech Stack

- **Frontend**: Streamlit (Prototype), React (Future)
- **Backend**: FastAPI / Flask
- **NLP Models**:
  - `distilBERT` / `RoBERTa` – for emotion and sentiment analysis
  - `BART` (zero-shot) – for beat classification
  - GPT-4 – for AI-generated rewrites
- **Tools**: SpaCy, Regex, Matplotlib/Plotly for visualizations

---

## 🧾 Project Roadmap

- **Phase 1**: Format checker + emotion graph (Streamlit prototype)
- **Phase 2**: Add beat detection + scene type classification
- **Phase 3**: Integrate GPT-based rewrites + user feedback loop
- **Phase 4**: User authentication, project saving, genre-based models

---

## 📂 Repository Structure (Expected)

```bash
FilmLab-ScriptWhisper/
├── data/                 # Sample screenplay scripts
├── models/               # NLP models and inference utilities
├── utils/                # Format checkers, preprocessors, etc.
├── app/                  # Streamlit or web app components
├── README.md             # Project overview
└── requirements.txt      # Dependencies
