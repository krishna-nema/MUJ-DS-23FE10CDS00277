# MailTone AI — Intelligent Email Tone & Intent Analyzer

## Student Details

- **Name:** Krishna Nema
- **Registration Number:** 23FE10CDS00277
- **Branch:** Data Science
- **Batch:** F
- **Project Title:** MailTone AI — Intelligent Email Tone & Intent Analyzer
- **GitHub Username:** krishna-nema

## Project Overview

MailTone AI is an NLP-based application that analyzes professional emails to identify tone-related indicators, sentiment, intent, and potential communication risks. It combines traditional Natural Language Processing techniques with Generative AI to help users understand how their messages may be perceived and improve their professional communication.

## Objectives

- Analyze email sentiment and linguistic features.
- Identify tone-related indicators, including urgency, formality, and aggressive wording.
- Interpret the sender's likely intent.
- Estimate possible recipient perception.
- Identify potential communication risks.
- Suggest improvements and generate a more professional email.

## Key Features

- **Sentiment Analysis:** Uses TextBlob to estimate the sentiment of an email.
- **Keyword Extraction:** Uses TF-IDF to identify important terms.
- **Linguistic Analysis:** Examines urgency, formality, and aggressive wording.
- **Readability Analysis:** Estimates how easy the email is to read.
- **Communication Risk Estimation:** Calculates a heuristic risk score from selected linguistic signals.
- **Generative AI Analysis:** Uses the Google Gemini API for contextual tone and intent interpretation.
- **Email Rewriting:** Suggests a more professional version while aiming to preserve the original meaning.
- **Interactive Dashboard:** Provides results through a Streamlit web interface.

## Technology Stack

- **Programming Language:** Python
- **Frontend:** Streamlit
- **Traditional NLP:** TextBlob, Scikit-learn, TF-IDF
- **Generative AI:** Google Gemini API, Google GenAI SDK
- **Structured Output:** Pydantic
- **Configuration:** PyYAML, python-dotenv

## Project Structure

```text
MailTone-AI/
├── app.py
├── src/
│   ├── __init__.py
│   ├── nlp_processor.py
│   └── llm_analyzer.py
├── config/
│   └── config.yaml
├── prompts/
│   └── email_analysis.txt
├── presentations/
├── README.md
├── requirements.txt
├── .env.example
└── .gitignore
```

The repository also includes the required Batch F folders: `assignments/`, `notebooks/`, `code/`, `resources/`, and `capstone/`.

## Installation and Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/krishna-nema/MUJ-DS-23FE10CDS00277.git
   ```

2. Navigate to the project directory:

   ```bash
   cd MUJ-DS-23FE10CDS00277
   ```

3. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   ```

   On Windows:

   ```bash
   venv\Scripts\activate
   ```

4. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Create a `.env` file based on `.env.example` and add your Gemini API key:

   ```text
   GEMINI_API_KEY=your_api_key_here
   ```

6. Run the application:

   ```bash
   streamlit run app.py
   ```

## Usage

1. Launch the Streamlit application.
2. Enter or paste an email into the text area.
3. Click the analysis button.
4. Review the traditional NLP metrics and Gemini-generated contextual analysis.
5. Examine the suggested improvements and professionally rewritten email.

## Limitations

- Tone and recipient perception can be subjective.
- Rule-based linguistic indicators may miss context.
- Communication risk scores are heuristic estimates, not scientifically validated measurements.
- Gemini analysis requires API access and is subject to the selected model's availability and usage limits.
- The current implementation primarily focuses on English-language emails.

## Future Scope

- Gmail and Outlook integration.
- Multilingual email analysis.
- Personalized writing styles.
- Batch email analysis.
- Email history analytics.
- Machine-learning-based tone classification.

## Security

Never commit your `.env` file, API keys, or other secrets to GitHub. The `.gitignore` file excludes sensitive configuration and virtual-environment files.

## Acknowledgement

Developed as an academic NLP project exploring the integration of traditional Natural Language Processing and Generative AI for professional communication analysis.
