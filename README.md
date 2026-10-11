# MailTone AI — Intelligent Email Tone & Intent Analyzer

## Student Details

- **Name:** Krishna Nema
- **Registration Number:** 23FE10CDS00277
- **Branch:** Data Science
- **Batch:** F
- **Project Title:** MailTone AI — Intelligent Email Tone & Intent Analyzer
- **GitHub Username:** [krishna-nema](https://github.com/krishna-nema)
- **Training Program:** To be updated

## 1. Project Overview

MailTone AI is an NLP-based application that analyzes the tone, sentiment, intent, and communication style of email messages. It helps users understand how their emails may be perceived by recipients and provides suggestions to improve clarity, professionalism, and effectiveness.

The application combines traditional Natural Language Processing (NLP) techniques with Google's Gemini API to generate contextual email analysis and improvement suggestions.

## 2. Objectives

- Analyze the sentiment and tone of email messages.
- Identify important keywords and potential urgency.
- Evaluate formality, readability, and potentially aggressive language.
- Understand email intent and communication context.
- Suggest improvements to make emails clearer and more professional.
- Provide an interactive interface for analyzing email content.

## 3. Key Features

- **Sentiment Analysis:** Estimates the emotional polarity of email text.
- **Keyword Extraction:** Identifies important terms using TF-IDF.
- **Tone Analysis:** Evaluates the communication style and formality of an email.
- **Intent Analysis:** Uses an LLM to interpret the context and likely purpose of an email.
- **Urgency and Risk Indicators:** Highlights potentially urgent wording or communication risks.
- **Email Improvement:** Generates suggestions and a revised version of the email.
- **Interactive Dashboard:** Provides a user-friendly interface built with Streamlit.

## 4. Technology Stack

- **Programming Language:** Python
- **Frontend / Interface:** Streamlit
- **Natural Language Processing:** TextBlob
- **Machine Learning:** Scikit-learn
- **Keyword Extraction:** TF-IDF
- **Large Language Model:** Google Gemini API
- **Configuration:** YAML
- **Environment Variables:** python-dotenv

## 5. Repository Structure

```text
MUJ-DS-23FE10CDS00277/
├── README.md
├── code/
│   ├── app.py
│   ├── requirements.txt
│   ├── src/
│   │   ├── __init__.py
│   │   ├── nlp_processor.py
│   │   └── llm_analyzer.py
│   ├── config/
│   │   └── config.yaml
│   └── prompts/
│       └── email_analysis.txt
├── capstone/
│   └── project-overview.md
├── presentations/
│   ├── presentation files
│   └── presentation speech
├── resources/
│   └── screenshots and sample results
├── .env.example
└── .gitignore
```

*Note: The presentation and resource entries above describe the intended contents; keep the folder contents and filenames consistent with the actual files uploaded to the repository.*

## 6. Installation and Setup

### Prerequisites

- Python 3.10 or a compatible version supported by the project's dependencies
- Git
- A Google Gemini API key

### Step 1: Clone the Repository

```bash
git clone https://github.com/krishna-nema/MUJ-DS-23FE10CDS00277.git
cd MUJ-DS-23FE10CDS00277
```

### Step 2: Create and Activate a Virtual Environment

On Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r code\requirements.txt
```

### Step 4: Configure the API Key

1. Create a copy of `.env.example` in the repository root and name it `.env`.
2. Open `.env` and add your Gemini API key using the variable expected by the application.

Example:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

Replace the placeholder with your actual API key. **Never upload your real `.env` file or expose your API key publicly.**

### Step 5: Run the Application

```bash
cd code
streamlit run app.py
```

The application should open in your browser. If it does not, use the local URL displayed in the terminal.

## 7. How It Works

1. The user enters an email message into the Streamlit interface.
2. The NLP processing module extracts linguistic information, sentiment, and relevant keywords.
3. The application evaluates communication characteristics using its analysis logic.
4. The Gemini API provides contextual analysis of the email's tone and intent.
5. The application displays the results and suggestions for improving the message.

## 8. Limitations

- Analysis results may vary depending on wording and context.
- Sentiment and tone detection may misinterpret sarcasm, cultural nuances, or ambiguous language.
- LLM-generated interpretations and suggestions may not always be accurate.
- Contextual analysis requires a valid API key and an available API service.
- The application is an assistive tool and should not be treated as a definitive judgment of the sender's intentions.

## 9. Future Scope

- Support for multiple languages.
- Integration with email platforms.
- More detailed emotion and intent classification.
- User-defined tone preferences.
- Expanded evaluation using a labeled email dataset.
- Enhanced privacy controls and deployment options.

## 10. Security and Privacy

- API credentials must be stored in a local `.env` file.
- The `.env` file and virtual environment must not be committed to GitHub.
- Users should avoid submitting confidential or sensitive email content to external AI services unless they understand the applicable data-handling implications.

## 11. Project Deliverables

The repository is intended to contain the project source code, capstone documentation, presentation materials, screenshots, and sample results. Refer to the `code/`, `capstone/`, `presentations/`, and `resources/` directories for the corresponding materials.

---

**Project:** MailTone AI — Intelligent Email Tone & Intent Analyzer  
**Student:** Krishna Nema  
**Registration Number:** 23FE10CDS00277  
**Branch:** Data Science | **Batch:** F
