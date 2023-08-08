import streamlit as st

# from knowledge_gpt.components.faq import faq
from dotenv import load_dotenv
import os

load_dotenv()


def sidebar():
    with st.sidebar:
        st.markdown(
            "## How to use\n"
            "1. Enter your [OpenAI API key](https://platform.openai.com/account/api-keys) below.\n"  # noqa: E501
            "2. Enter your [Deepgram API key](https://developers.deepgram.com/docs/authenticating) below.\n"  # noqa: E501
            "3. Paste the link of the YouTube video you want to analyze.\n"
            "4. Click Analyze!\n"
        )
        api_key_input = st.text_input(
            "OpenAI API Key",
            type="password",
            placeholder="Paste your OpenAI API key here (sk-...)",
            help="You can get your API key from https://platform.openai.com/account/api-keys.",  # noqa: E501
            value=os.environ.get("OPENAI_API_KEY", None)
            or st.session_state.get("OPENAI_API_KEY", ""),
        )
        deepgram_api_key = st.text_input(
            "Deepgram API Key",
            type="password",
            placeholder="Paste your Deepgram API key here (sk-...)",
            help="You can get your API key from https://developers.deepgram.com/docs/authenticating.",  # noqa: E501
            value=os.environ.get("DEEPGRAM_API_KEY", None)
            or st.session_state.get("DEEPGRAM_API_KEY", ""),
        )
        st.session_state["OPENAI_API_KEY"] = api_key_input
        st.session_state["DEEPGRAM_API_KEY"] = deepgram_api_key

        st.markdown("---")

        st.markdown("# About")
        st.markdown(
            "This tool allows you to quickly extract stock predections "
            "from your favourite (Jim Cramer) YouTube videos. "
            "It relies on a combination of OpenAI's GPT-3.5 and Deepgram's speech-to-text API "
            "along with [deberta-v3-base-finetuned-finance-text-classification](https://huggingface.co/nickmuchi/deberta-v3-base-finetuned-finance-text-classification) model from HuggingFace "
            "to generate predictions from the video's audio. This is still a work in progress, "
            "so might not be perfect. Feel free to contribute to the project on [GitHub]()"
        )
        st.markdown(
            "Note: The predictions are not financial advice. Invest at your own risk."
        )
        st.markdown("Made by [Saarth Shah](https://twitter.com/saarth28)")
        st.markdown("---")

        # faq()