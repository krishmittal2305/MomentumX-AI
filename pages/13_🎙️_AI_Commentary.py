import streamlit as st
import random

st.set_page_config(
    page_title="AI Commentary",
    page_icon="🎙️",
    layout="wide"
)

st.title("🎙️ AI Commentary Generator")

team1 = st.text_input("Batting Team", "RCB")
team2 = st.text_input("Bowling Team", "CSK")

over = st.slider("Current Over", 1, 20, 16)

runs = st.slider("Runs This Over", 0, 36, 12)

wicket = st.checkbox("Wicket Fallen?")

commentaries = [

    f"{team1} are trying to accelerate heavily in the death overs.",

    f"Momentum appears to be shifting towards {team1}.",

    f"{team2} desperately need a breakthrough in this phase.",

    f"This over could completely change the match trajectory.",

    f"The pressure is increasing dramatically under the lights."

]

if wicket:

    commentaries.append(
        f"Massive wicket! Momentum suddenly swings back towards {team2}."
    )

if runs >= 15:

    commentaries.append(
        f"Explosive over from {team1}! The momentum engine is glowing red hot."
    )

if st.button("Generate AI Commentary"):

    st.success(random.choice(commentaries))