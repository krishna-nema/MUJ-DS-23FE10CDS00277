import json
import os
from pathlib import Path

import yaml
from dotenv import load_dotenv
from google import genai
from pydantic import BaseModel


BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / ".env")


# ---------------------------------------------------------
# Load Configuration
# ---------------------------------------------------------

with open(
    BASE_DIR / "config" / "config.yaml",
    "r",
    encoding="utf-8"
) as file:
    config = yaml.safe_load(file)


# ---------------------------------------------------------
# Load Prompt
# ---------------------------------------------------------

with open(
    BASE_DIR / "prompts" / "email_analysis.txt",
    "r",
    encoding="utf-8"
) as file:
    SYSTEM_PROMPT = file.read()


# ---------------------------------------------------------
# Structured Gemini Response
# ---------------------------------------------------------

class EmailAnalysis(BaseModel):

    primary_tone: str

    secondary_tones: list[str]

    sentiment: str

    intent: str

    professionalism_score: int

    urgency_score: int

    politeness_score: int

    passive_aggressive_likelihood: int

    recipient_perception: str

    communication_risks: list[str]

    improvement_suggestions: list[str]

    improved_email: str


# ---------------------------------------------------------
# Gemini Analysis
# ---------------------------------------------------------

def analyze_with_llm(email, nlp_results):

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        return None

    try:

        client = genai.Client(
            api_key=api_key
        )

        user_data = {
            "email": email,
            "traditional_nlp_analysis": nlp_results
        }

        prompt = f"""
{SYSTEM_PROMPT}

Analyze the following email.

EMAIL:
{email}

TRADITIONAL NLP ANALYSIS:
{json.dumps(nlp_results, indent=2)}

Use the traditional NLP analysis as supporting evidence,
but perform your own contextual interpretation of the email.

Keep all scores between 0 and 100.

Preserve the original meaning when creating the improved email.
"""

        response = client.models.generate_content(

            model=config["llm"]["model"],

            contents=prompt,

            config={
                "response_mime_type": "application/json",
                "response_schema": EmailAnalysis
            }
        )

        # Gemini SDK provides the structured result
        if getattr(response, "parsed", None):

            result = response.parsed

            if isinstance(result, EmailAnalysis):
                return result.model_dump()

            return result

        # Fallback to JSON text if parsed output is unavailable
        raw_output = response.text.strip()

        return json.loads(raw_output)

    except Exception as error:

        return {
            "error": str(error)
        }