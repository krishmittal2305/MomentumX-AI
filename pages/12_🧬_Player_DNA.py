import streamlit as st
import pandas as pd
import random

st.set_page_config(
    page_title="Player DNA",
    page_icon="🧬",
    layout="wide"
)

st.markdown("""
<style>

.stApp {
    background:
        linear-gradient(135deg, #020617, #111827, #000000);
    color: white;
}

.title {
    font-size: 54px;
    font-weight: 950;
    background: linear-gradient(90deg, #38bdf8, #a855f7, #facc15);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.dna-card {
    padding: 35px;
    border-radius: 30px;

    background:
        linear-gradient(135deg,
        rgba(59,130,246,0.14),
        rgba(168,85,247,0.12),
        rgba(250,204,21,0.08));

    border: 1px solid rgba(255,255,255,0.15);

    box-shadow:
        0 0 25px rgba(59,130,246,0.25),
        0 0 45px rgba(168,85,247,0.18);

}

.trait {
    padding: 14px 18px;
    border-radius: 18px;
    margin-bottom: 12px;

    background:
        rgba(255,255,255,0.08);

    border:
        1px solid rgba(255,255,255,0.12);

    font-size: 18px;
}

</style>
""", unsafe_allow_html=True)

df = pd.read_csv("final_momentumx_dataset.csv")

st.markdown(
    '<div class="title">🧬 Player DNA Intelligence</div>',
    unsafe_allow_html=True
)

players = sorted(df["batter"].dropna().unique())

player = st.selectbox(
    "Select Player",
    players
)

player_df = df[df["batter"] == player]

runs = int(player_df["batsman_runs"].sum())
impact = round(player_df["impact_score"].mean(),2)
pressure = round(player_df["pressure_score"].mean(),2)
momentum = round(player_df["momentum"].mean(),2)

traits = []

if impact >= 2:
    traits.append("🔥 Clutch Performer")

if momentum >= 0.7:
    traits.append("⚡ Momentum Accelerator")

if pressure >= 5:
    traits.append("🧠 Pressure Warrior")

if runs >= 500:
    traits.append("🏏 Run Machine")

if len(traits) < 2:
    traits.append("🎯 Match Stabilizer")

descriptions = [

    "Thrives during difficult match situations.",

    "Capable of shifting momentum rapidly.",

    "Maintains scoring consistency under pressure.",

    "Creates aggressive scoring acceleration.",

    "Acts as a stabilizer during collapses."

]

st.write("")

st.markdown(f"""
<div class="dna-card">

<h1>{player}</h1>

<p style="font-size:20px;">
MomentumX AI Personality Profile
</p>

<hr>

<p>
Runs: <b>{runs}</b><br>
Impact Score: <b>{impact}</b><br>
Pressure Score: <b>{pressure}</b><br>
Momentum Score: <b>{momentum}</b>
</p>

<hr>

</div>
""", unsafe_allow_html=True)

st.write("")

for trait in traits:

    st.markdown(f"""
    <div class="trait">
    {trait}
    </div>
    """, unsafe_allow_html=True)

st.write("")

st.info(random.choice(descriptions))