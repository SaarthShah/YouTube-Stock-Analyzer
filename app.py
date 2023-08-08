import streamlit as st

st.set_page_config(page_title="Stock Analyzer", page_icon="📈", layout="wide")
st.header("Stock Analyzer 💎🙌")
st.markdown(
    "Stock Analyzer allows you to quickly extract stock predections "
    "from your favourite (Jim Cramer) YouTube videos. 📈💎🙌🦍🤝💪",
)




from components.sidebar import sidebar
sidebar()

openai_api_key = st.session_state.get("OPENAI_API_KEY")


if not openai_api_key:
    st.warning(
        "Enter your OpenAI API key in the sidebar. You can get a key at"
        " https://platform.openai.com/account/api-keys."
    )

deepgram_api_key = st.session_state.get("DEEPGRAM_API_KEY")

if not deepgram_api_key:
    st.warning(
        "Enter your Deepgram API key in the sidebar. You can get a key at"
        " https://developers.deepgram.com/getting-started."
    )

if openai_api_key and deepgram_api_key:
    from components.analyzer import analyzer

    analyzer()
else:
    st.warning(
        "Enter your OpenAI and Deepgram API keys in the sidebar to get started."
    )