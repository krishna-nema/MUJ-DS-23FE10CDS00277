# MailTone AI — Project Overview

## Problem Statement
Written communication can be misunderstood because emails do not convey voice tone, facial expressions, or immediate feedback.

## Objectives
- Analyze email sentiment and linguistic features.
- Identify tone-related indicators and sender intent.
- Estimate possible recipient perception.
- Identify communication risks.
- Suggest improvements and rewrite emails professionally.

## Methodology
The application combines traditional NLP techniques, including sentiment analysis, TF-IDF keyword extraction, linguistic indicators, and readability analysis, with Google Gemini for contextual interpretation and email rewriting.

## Technology Stack
Python, Streamlit, TextBlob, Scikit-learn, TF-IDF, Google Gemini API, Pydantic, PyYAML, and python-dotenv.

## Limitations
Tone perception is subjective, rule-based indicators may miss context, heuristic scores are estimates, and Gemini analysis depends on API availability.
