import subprocess

# Replace this with your GitHub repo name
repo_name = "BhavyaSamhithaMallineni/FilmLAB" 

# Your to-do list (add or modify as needed)
todos = [
    "[Phase 0] Create GitHub repository and initialize with README",
    "[Phase 0] Set up Python virtual environment and install core libraries",
    "[Phase 0] Install NLP dependencies: transformers, spacy, nltk, textstat",
    "[Phase 0] Initialize Streamlit base app for UI development",
    "[Phase 1.1] Build Format Checker using Regex and SpaCy",
    "[Phase 1.2] Implement Sentiment Analyzer using distilBERT",
    "[Phase 1.3] Extract and split screenplay into scenes/pages",
    "[Phase 1.4] Classify scene types using BART zero-shot model",
    "[Phase 1.5] Evaluate and score dialogue realism with textstat",
    "[Phase 1.6] Add GPT-powered dialogue and scene rewrites",
    "[Phase 2.1] Create Streamlit upload UI (PDF/text)",
    "[Phase 2.2] Display screenplay structure and feedback in UI",
    "[Phase 2.3] Visualize emotional arc with Matplotlib or Plotly",
    "[Phase 2.4] Add beat classification results to Streamlit output",
    "[Phase 2.5] Add download/export feature for analysis report",
    "[Phase 3.1] Add writing tooltips explaining each suggestion",
    "[Phase 3.2] Embed micro-tutorials or screenwriting theory links",
    "[Phase 3.3] Build reference panel with Save the Cat/Truby concepts",
    "[Phase 4.1] Deploy MVP app to Streamlit Cloud or Render",
    "[Phase 4.2] Create user feedback form in UI",
    "[Phase 4.3] Gather early testers from Reddit, Discord, LinkedIn",
    "[Phase 4.4] Analyze feedback and define improvements",
    "[Phase 5.1] Train or integrate genre-specific beat models",
    "[Phase 5.2] Add character voice consistency checker",
    "[Phase 5.3] Expand support to full-screenplay documents",
    "[Phase 5.4] Build custom visualization for Save the Cat beats"
]

# Loop through the tasks and create GitHub issues
for task in todos:
    command = [
        "gh", "issue", "create",
        "--repo", repo_name,
        "--title", task,
        "--body", "Auto-generated from FilmLab development To-Do list."
    ]
    subprocess.run(command)

print("✅ Issues created successfully!")
