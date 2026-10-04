# 📧 MailTone AI

### Intelligent Email Tone & Intent Analyzer

MailTone AI is an NLP and Generative AI based application that analyzes professional emails and predicts how they may be perceived by the recipient.

The system combines traditional Natural Language Processing techniques with Google's Gemini API to provide deeper contextual analysis and suggestions for improving email communication.

---

## 🚀 Features

### Traditional NLP Analysis

- Text preprocessing and normalization
- Word and sentence analysis
- Sentiment analysis using TextBlob
- TF-IDF based keyword extraction
- Urgency indicator detection
- Formal language detection
- Aggressive language detection
- Readability analysis
- Average sentence length
- Formality scoring
- Communication risk estimation

### Generative AI Analysis

Gemini is used for contextual analysis of:

- Primary tone
- Secondary tones
- Sender intent
- Professionalism
- Politeness
- Urgency
- Passive-aggressive likelihood
- Recipient perception
- Communication risks
- Improvement suggestions
- Professionally improved email

---

## 🧠 System Architecture

```text
                    Email Input
                         │
                         ▼
              ┌─────────────────────┐
              │   Text Preprocessing │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │   Traditional NLP   │
              │                     │
              │ • Sentiment         │
              │ • TF-IDF            │
              │ • Readability       │
              │ • Formality         │
              │ • Urgency           │
              │ • Aggression        │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │     Gemini LLM      │
              │                     │
              │ Contextual Analysis │
              │ Structured Output   │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │    MailTone AI UI   │
              │                     │
              │ Tone • Intent       │
              │ Risks • Suggestions │
              │ Improved Email      │
              └─────────────────────┘