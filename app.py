import streamlit as st

from src.nlp_processor import analyze_email
from src.llm_analyzer import analyze_with_llm


# ---------------------------------------------------------
# Page Configuration
# ---------------------------------------------------------

st.set_page_config(
    page_title="MailTone AI",
    page_icon="📧",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ---------------------------------------------------------
# Custom Styling
# ---------------------------------------------------------

st.markdown(
    """
    <style>

    .main {
        padding-top: 1rem;
    }

    .hero {
        padding: 25px 30px;
        border-radius: 16px;
        margin-bottom: 25px;
        background: linear-gradient(
            135deg,
            rgba(49, 51, 63, 0.8),
            rgba(25, 28, 40, 0.9)
        );
        border: 1px solid rgba(255,255,255,0.08);
    }

    .hero h1 {
        margin-bottom: 5px;
        font-size: 42px;
    }

    .hero p {
        font-size: 17px;
        color: #b8bdc9;
        margin-bottom: 0;
    }

    .section-title {
        font-size: 25px;
        font-weight: 700;
        margin-top: 25px;
        margin-bottom: 15px;
    }

    .score-card {
        padding: 18px;
        border-radius: 14px;
        background: rgba(35, 38, 50, 0.8);
        border: 1px solid rgba(255,255,255,0.08);
        text-align: center;
        min-height: 115px;
    }

    .score-label {
        color: #aeb4c0;
        font-size: 14px;
        margin-bottom: 8px;
    }

    .score-value {
        font-size: 27px;
        font-weight: 700;
    }

    .keyword {
        display: inline-block;
        padding: 6px 12px;
        margin: 4px;
        border-radius: 20px;
        background: rgba(75, 120, 220, 0.18);
        border: 1px solid rgba(75, 120, 220, 0.35);
        font-size: 14px;
    }

    .footer {
        text-align: center;
        color: #777d89;
        margin-top: 40px;
        padding: 20px;
        font-size: 13px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ---------------------------------------------------------
# Header
# ---------------------------------------------------------

st.markdown(
    """
    <div class="hero">
        <h1>📧 MailTone AI</h1>
        <p>
            Intelligent Email Tone & Intent Analyzer
        </p>
        <p>
            Understand how your email may be perceived
            before you send it.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)


# ---------------------------------------------------------
# Email Input
# ---------------------------------------------------------

st.markdown(
    '<div class="section-title">✉️ Enter Your Email</div>',
    unsafe_allow_html=True
)

email = st.text_area(
    "Email content",
    height=230,
    label_visibility="collapsed",
    placeholder=(
        "Paste your email here...\n\n"
        "Example:\n"
        "I have already asked you three times to send "
        "the report. Please send it today because I "
        "need to submit it before the deadline."
    )
)

analyze_button = st.button(
    "🔍 Analyze Email",
    type="primary",
    use_container_width=True
)


# ---------------------------------------------------------
# Analysis
# ---------------------------------------------------------

if analyze_button:

    if not email.strip():

        st.warning(
            "Please enter an email before analyzing it."
        )

    else:

        with st.spinner(
            "Analyzing your email with NLP and AI..."
        ):

            nlp_results = analyze_email(email)

            llm_results = analyze_with_llm(
                email,
                nlp_results
            )

        # -------------------------------------------------
        # Traditional NLP
        # -------------------------------------------------

        st.markdown(
            '<div class="section-title">'
            '📊 Traditional NLP Analysis'
            '</div>',
            unsafe_allow_html=True
        )

        col1, col2, col3, col4 = st.columns(4)

        col1.metric(
            "Words",
            nlp_results["word_count"]
        )

        col2.metric(
            "Sentences",
            nlp_results["sentence_count"]
        )

        col3.metric(
            "Sentiment",
            nlp_results["sentiment"]["label"]
        )

        col4.metric(
            "Urgency Indicators",
            nlp_results["urgency_indicators"]
        )

        # -------------------------------------------------
        # Keywords
        # -------------------------------------------------

        st.markdown(
            '<div class="section-title">'
            '🔑 Important Keywords'
            '</div>',
            unsafe_allow_html=True
        )

        if nlp_results["keywords"]:

            keyword_html = ""

            for keyword in nlp_results["keywords"]:

                keyword_html += (
                    f'<span class="keyword">{keyword}</span>'
                )

            st.markdown(
                keyword_html,
                unsafe_allow_html=True
            )

        else:

            st.info(
                "No significant keywords detected."
            )

        # -------------------------------------------------
        # Linguistic Indicators
        # -------------------------------------------------

        st.markdown(
            '<div class="section-title">'
            '📈 Linguistic Indicators'
            '</div>',
            unsafe_allow_html=True
        )

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Formal Indicators",
            nlp_results["formal_indicators"]
        )

        col2.metric(
            "Aggressive Indicators",
            nlp_results["aggressive_indicators"]
        )

        col3.metric(
            "Sentiment Polarity",
            nlp_results["sentiment"]["polarity"]
        )

        # -------------------------------------------------
        # Advanced NLP Metrics
        # -------------------------------------------------

        st.markdown(
            '<div class="section-title">'
            '🧠 Advanced NLP Metrics'
            '</div>',
            unsafe_allow_html=True
        )

        col1, col2, col3, col4 = st.columns(4)

        col1.metric(
            "Readability",
            f'{nlp_results["readability_score"]}/100'
        )

        col2.metric(
            "Avg. Sentence Length",
            f'{nlp_results["average_sentence_length"]} words'
        )

        col3.metric(
            "Formality Score",
            f'{nlp_results["formality_score"]}/100'
        )

        col4.metric(
            "Communication Risk",
            f'{nlp_results["communication_risk_score"]}/100'
        )

        st.progress(
            int(nlp_results["readability_score"]),
            text="Readability"
        )

        st.progress(
            int(nlp_results["formality_score"]),
            text="Formality"
        )

        st.progress(
            int(nlp_results["communication_risk_score"]),
            text="Communication Risk"
        )

        # -------------------------------------------------
        # AI Communication Analysis
        # -------------------------------------------------

        st.markdown(
            '<div class="section-title">'
            '🤖 AI Communication Analysis'
            '</div>',
            unsafe_allow_html=True
        )

        if llm_results is None:

            st.error(
                "Gemini API key is not configured."
            )

        elif "error" in llm_results:

            st.error(
                "Gemini analysis failed."
            )

            st.code(
                llm_results["error"]
            )

        else:

            # ---------------------------------------------
            # AI Score Cards
            # ---------------------------------------------

            col1, col2, col3, col4 = st.columns(4)

            with col1:

                st.markdown(
                    f"""
                    <div class="score-card">
                        <div class="score-label">
                            🎭 Primary Tone
                        </div>
                        <div class="score-value">
                            {llm_results["primary_tone"]}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            with col2:

                st.markdown(
                    f"""
                    <div class="score-card">
                        <div class="score-label">
                            💼 Professionalism
                        </div>
                        <div class="score-value">
                            {llm_results["professionalism_score"]}/100
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            with col3:

                st.markdown(
                    f"""
                    <div class="score-card">
                        <div class="score-label">
                            🤝 Politeness
                        </div>
                        <div class="score-value">
                            {llm_results["politeness_score"]}/100
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            with col4:

                st.markdown(
                    f"""
                    <div class="score-card">
                        <div class="score-label">
                            ⚡ Urgency
                        </div>
                        <div class="score-value">
                            {llm_results["urgency_score"]}/100
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            # ---------------------------------------------
            # Communication Scores
            # ---------------------------------------------

            st.markdown(
                '<div class="section-title">'
                '📊 Communication Scores'
                '</div>',
                unsafe_allow_html=True
            )

            st.write("Professionalism")

            st.progress(
                min(
                    max(
                        int(
                            llm_results[
                                "professionalism_score"
                            ]
                        ),
                        0
                    ),
                    100
                )
            )

            st.write("Politeness")

            st.progress(
                min(
                    max(
                        int(
                            llm_results[
                                "politeness_score"
                            ]
                        ),
                        0
                    ),
                    100
                )
            )

            st.write("Urgency")

            st.progress(
                min(
                    max(
                        int(
                            llm_results[
                                "urgency_score"
                            ]
                        ),
                        0
                    ),
                    100
                )
            )

            # ---------------------------------------------
            # Intent
            # ---------------------------------------------

            st.markdown(
                '<div class="section-title">'
                '🎯 Sender Intent'
                '</div>',
                unsafe_allow_html=True
            )

            st.info(
                llm_results["intent"]
            )

            # ---------------------------------------------
            # Recipient Perception
            # ---------------------------------------------

            st.markdown(
                '<div class="section-title">'
                '🧠 Recipient Perception'
                '</div>',
                unsafe_allow_html=True
            )

            st.info(
                llm_results["recipient_perception"]
            )

            # ---------------------------------------------
            # Communication Risks
            # ---------------------------------------------

            st.markdown(
                '<div class="section-title">'
                '⚠️ Communication Risks'
                '</div>',
                unsafe_allow_html=True
            )

            risks = llm_results.get(
                "communication_risks",
                []
            )

            if risks:

                for risk in risks:
                    st.warning(risk)

            else:

                st.success(
                    "No major communication risks detected."
                )

            # ---------------------------------------------
            # Suggestions
            # ---------------------------------------------

            st.markdown(
                '<div class="section-title">'
                '💡 Improvement Suggestions'
                '</div>',
                unsafe_allow_html=True
            )

            suggestions = llm_results.get(
                "improvement_suggestions",
                []
            )

            if suggestions:

                for suggestion in suggestions:
                    st.write(
                        f"• {suggestion}"
                    )

            else:

                st.success(
                    "No improvement suggestions needed."
                )

            # ---------------------------------------------
            # Improved Email
            # ---------------------------------------------

            st.markdown(
                '<div class="section-title">'
                '✍️ Improved Email'
                '</div>',
                unsafe_allow_html=True
            )

            st.success(
                llm_results["improved_email"]
            )


# ---------------------------------------------------------
# Footer
# ---------------------------------------------------------

st.markdown(
    """
    <div class="footer">
        MailTone AI • NLP + Generative AI
        <br>
        Analyze • Understand • Improve
    </div>
    """,
    unsafe_allow_html=True
)