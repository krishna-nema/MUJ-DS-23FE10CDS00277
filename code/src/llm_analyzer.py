
import json
import os
from pathlib import Path

import yaml
from dotenv import load_dotenv
from google import genai
from pydantic import BaseModel


# Directory paths
# llm_analyzer.py is inside: code/src/
CODE_DIR = Path(__file__).resolve().parent.parent
PROJECT_ROOT = CODE_DIR.parent

# Load API key from the repository root
load_dotenv(PROJECT_ROOT / ".env")

# Load configuration from code/config/
with open(
    CODE_DIR / "config" / "config.yaml",
    "r",
    encoding="utf-8",
) as file:
    config = yaml.safe_load(file)

# Load prompt from code/prompts/
with open(
    CODE_DIR / "prompts" / "email_analysis.txt",
    "r",
    encoding="utf-8",
) as file:
    SYSTEM_PROMPT = file.read()


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


def analyze_with_llm(email, nlp_results):
    """Analyze an email using Gemini and traditional NLP results."""

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        return {
            "error": (
                "Gemini API key is not configured. "
                "Check that GEMINI_API_KEY is set in the "
                "repository-root .env file."
            )
        }

    try:
        client = genai.Client(api_key=api_key)

        prompt = f"""
{SYSTEM_PROMPT}

Analyze the following email.

EMAIL:
{email}

TRADITIONAL NLP ANALYSIS:
{json.dumps(nlp_results, indent=2, ensure_ascii=False)}

Instructions:
- Use the traditional NLP results as supporting evidence.
- Perform your own contextual interpretation.
- Keep all scores between 0 and 100.
- Preserve the original meaning when rewriting.
- Do not invent information.
- Return valid structured JSON matching the requested schema.
"""

        response = client.models.generate_content(
            model=config["llm"]["model"],
            contents=prompt,
            config={
                "response_mime_type": "application/json",
                "response_schema": EmailAnalysis,
                "max_output_tokens": config["llm"].get(
                    "max_output_tokens", 1200
                ),
            },
        )

        if getattr(response, "parsed", None) is not None:
            result = response.parsed

            if isinstance(result, EmailAnalysis):
                return result.model_dump()

            if isinstance(result, dict):
                return result

        if not response.text:
            return {"error": "Gemini returned an empty response."}

        return EmailAnalysis.model_validate_json(
            response.text
        ).model_dump()

    except Exception as error:
        return {"error": f"{type(error).__name__}: {error}"}
