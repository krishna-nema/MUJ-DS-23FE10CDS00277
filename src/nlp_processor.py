import re
from collections import Counter

from textblob import TextBlob
from sklearn.feature_extraction.text import TfidfVectorizer


URGENCY_WORDS = {
    "urgent", "urgently", "asap", "immediately",
    "today", "now", "deadline", "important",
    "priority", "quickly"
}

FORMAL_WORDS = {
    "please", "kindly", "request", "appreciate",
    "regards", "sincerely", "respectfully",
    "could", "would", "thank", "thankful"
}

AGGRESSIVE_WORDS = {
    "ridiculous", "unacceptable", "terrible",
    "obviously", "failure", "wrong", "never",
    "again", "stupid", "incompetent"
}


def clean_text(text):
    """Clean and normalize text."""

    text = text.lower()
    text = re.sub(r"\s+", " ", text)

    return text.strip()


def tokenize_text(text):
    """Extract word tokens."""

    return re.findall(
        r"\b[a-zA-Z]+\b",
        text.lower()
    )


def get_sentiment(text):
    """Calculate sentiment using TextBlob."""

    result = TextBlob(text)

    polarity = result.sentiment.polarity
    subjectivity = result.sentiment.subjectivity

    if polarity > 0.1:
        label = "Positive"
    elif polarity < -0.1:
        label = "Negative"
    else:
        label = "Neutral"

    return {
        "label": label,
        "polarity": round(polarity, 3),
        "subjectivity": round(subjectivity, 3)
    }


def get_keywords(text, top_n=8):
    """Extract important keywords using TF-IDF."""

    try:

        vectorizer = TfidfVectorizer(
            stop_words="english",
            max_features=50
        )

        matrix = vectorizer.fit_transform([text])

        scores = matrix.toarray()[0]
        words = vectorizer.get_feature_names_out()

        ranked = sorted(
            zip(words, scores),
            key=lambda item: item[1],
            reverse=True
        )

        return [
            word
            for word, score in ranked[:top_n]
        ]

    except ValueError:

        return []


def count_words(text, word_set):
    """Count linguistic indicators."""

    tokens = tokenize_text(text)

    counter = Counter(tokens)

    return sum(
        counter[word]
        for word in word_set
    )


def count_syllables(word):
    """Approximate syllable count for readability analysis."""

    word = word.lower()

    vowels = "aeiouy"
    count = 0
    previous_vowel = False

    for char in word:

        is_vowel = char in vowels

        if is_vowel and not previous_vowel:
            count += 1

        previous_vowel = is_vowel

    if word.endswith("e") and count > 1:
        count -= 1

    return max(count, 1)


def calculate_readability(text):
    """
    Calculate an approximate Flesch Reading Ease score.

    Higher score = easier to read.
    """

    words = tokenize_text(text)

    if not words:
        return 0

    sentences = [
        sentence
        for sentence in re.split(
            r"[.!?]+",
            text
        )
        if sentence.strip()
    ]

    sentence_count = max(len(sentences), 1)
    word_count = len(words)

    syllable_count = sum(
        count_syllables(word)
        for word in words
    )

    score = (
        206.835
        - 1.015 * (word_count / sentence_count)
        - 84.6 * (syllable_count / word_count)
    )

    return round(
        max(0, min(100, score)),
        1
    )


def calculate_formality_score(
    word_count,
    formal_count,
    aggressive_count
):
    """Estimate formality from linguistic indicators."""

    if word_count == 0:
        return 0

    formal_ratio = formal_count / word_count
    aggressive_ratio = aggressive_count / word_count

    score = 50 + (formal_ratio * 1000) - (
        aggressive_ratio * 1200
    )

    return round(
        max(0, min(100, score)),
        1
    )


def calculate_urgency_score(
    word_count,
    urgency_count
):
    """Estimate urgency intensity."""

    if word_count == 0:
        return 0

    score = (
        urgency_count / word_count
    ) * 1000

    return round(
        max(0, min(100, score)),
        1
    )


def calculate_aggressiveness_score(
    word_count,
    aggressive_count
):
    """Estimate aggressive language intensity."""

    if word_count == 0:
        return 0

    score = (
        aggressive_count / word_count
    ) * 1500

    return round(
        max(0, min(100, score)),
        1
    )


def calculate_risk_score(
    sentiment,
    aggressive_count,
    urgency_count,
    word_count
):
    """
    Estimate communication risk.

    This is a heuristic NLP score, not a clinical
    or psychological assessment.
    """

    risk = 0

    if sentiment["polarity"] < -0.2:
        risk += 25

    if aggressive_count > 0:
        risk += min(
            aggressive_count * 15,
            40
        )

    if urgency_count >= 2:
        risk += 15

    if urgency_count >= 4:
        risk += 10

    if word_count < 5:
        risk += 5

    return round(
        min(risk, 100),
        1
    )


def analyze_email(email):
    """Perform complete traditional NLP analysis."""

    cleaned = clean_text(email)

    tokens = tokenize_text(cleaned)

    word_count = len(tokens)

    sentences = [
        sentence
        for sentence in re.split(
            r"[.!?]+",
            email
        )
        if sentence.strip()
    ]

    sentence_count = len(sentences)

    sentiment = get_sentiment(cleaned)

    keywords = get_keywords(cleaned)

    urgency_count = count_words(
        cleaned,
        URGENCY_WORDS
    )

    formal_count = count_words(
        cleaned,
        FORMAL_WORDS
    )

    aggressive_count = count_words(
        cleaned,
        AGGRESSIVE_WORDS
    )

    average_sentence_length = round(
        word_count / max(sentence_count, 1),
        1
    )

    readability_score = calculate_readability(
        email
    )

    formality_score = calculate_formality_score(
        word_count,
        formal_count,
        aggressive_count
    )

    urgency_score = calculate_urgency_score(
        word_count,
        urgency_count
    )

    aggressiveness_score = calculate_aggressiveness_score(
        word_count,
        aggressive_count
    )

    risk_score = calculate_risk_score(
        sentiment,
        aggressive_count,
        urgency_count,
        word_count
    )

    return {

        "word_count": word_count,

        "sentence_count": sentence_count,

        "average_sentence_length":
            average_sentence_length,

        "readability_score":
            readability_score,

        "sentiment": sentiment,

        "keywords": keywords,

        "urgency_indicators":
            urgency_count,

        "formal_indicators":
            formal_count,

        "aggressive_indicators":
            aggressive_count,

        "formality_score":
            formality_score,

        "urgency_score":
            urgency_score,

        "aggressiveness_score":
            aggressiveness_score,

        "communication_risk_score":
            risk_score
    }