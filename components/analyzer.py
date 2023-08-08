import streamlit as st
import components.engine as engine

def analyzer():
    # allow users to enter a YouTube link
    youtube_link = st.text_input(
        "YouTube Link",
        placeholder="Paste the link of the YouTube video you want to analyze here.",
        value='https://www.youtube.com/watch?v=16SUWTGsDGI&ab_channel=CNBCTelevision',
    )
    # Analyze button
    if st.button("Analyze!"):
        if youtube_link:
            engine.engine(youtube_link)
        else:
            st.error("Please enter a YouTube link.")
        print("Analyze button clicked!")


    
