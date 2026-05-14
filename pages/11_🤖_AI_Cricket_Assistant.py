import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="AI Cricket Assistant",
    page_icon="🤖",
    layout="wide"
)

st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(circle at top left, rgba(59,130,246,0.18), transparent 28%),
        radial-gradient(circle at top right, rgba(168,85,247,0.18), transparent 30%),
        linear-gradient(135deg, #020617, #111827, #000000);
    color: white;
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #020617, #111827, #000000);
}

.title {
    font-size: 52px;
    font-weight: 950;
    background: linear-gradient(90deg, #38bdf8, #a855f7, #facc15);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.chat-box {
    padding: 30px;
    border-radius: 30px;
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.15);
    box-shadow: 0 20px 60px rgba(0,0,0,0.50);
}

.answer {
    padding: 22px;
    border-radius: 22px;
    background:
        linear-gradient(135deg,
        rgba(59,130,246,0.14),
        rgba(168,85,247,0.10));
    border: 1px solid rgba(255,255,255,0.12);
    margin-top: 20px;
    font-size: 18px;
    line-height: 1.8;
}

</style>
""", unsafe_allow_html=True)

df = pd.read_csv("final_momentumx_dataset.csv")

st.markdown(
    '<div class="title">🤖 AI Cricket Assistant</div>',
    unsafe_allow_html=True
)

st.caption(
    "Ask MomentumX AI anything about IPL momentum, players, pressure or teams."
)

st.write("")

st.markdown("""
<div class="chat-box">
<h3>Example Questions</h3>

• Who is the best batter?<br>
• Which team has highest momentum?<br>
• Who performs best under pressure?<br>
• Which team has highest collapse risk?<br>
• Who hits most boundaries?<br>
• Which player has highest impact score?<br>

</div>
""", unsafe_allow_html=True)

question = st.text_input(
    "Ask your cricket question"
)

if question:

    q = question.lower()

    answer = "I could not understand the question."

    # =========================
    # BEST BATTER
    # =========================

    if "best batter" in q or "top batter" in q:

        batter = (
            df.groupby("batter")["batsman_runs"]
            .sum()
            .sort_values(ascending=False)
            .index[0]
        )

        runs = (
            df.groupby("batter")["batsman_runs"]
            .sum()
            .sort_values(ascending=False)
            .iloc[0]
        )

        answer = f"""
        🏏 {batter} is currently the top batter in MomentumX AI analytics
        with {int(runs)} total runs.
        """

    # =========================
    # MOST BOUNDARIES
    # =========================

    elif "boundaries" in q:

        boundary_df = df[df["batsman_runs"] >= 4]

        player = (
            boundary_df.groupby("batter")
            .size()
            .sort_values(ascending=False)
            .index[0]
        )

        count = (
            boundary_df.groupby("batter")
            .size()
            .sort_values(ascending=False)
            .iloc[0]
        )

        answer = f"""
        🔥 {player} has produced the highest number of boundaries
        with {count} boundary events.
        """

    # =========================
    # HIGHEST MOMENTUM TEAM
    # =========================

    elif "highest momentum" in q or "strongest team" in q:

        team = (
            df.groupby("inning_team")["momentum"]
            .mean()
            .sort_values(ascending=False)
            .index[0]
        )

        score = (
            df.groupby("inning_team")["momentum"]
            .mean()
            .sort_values(ascending=False)
            .iloc[0]
        )

        answer = f"""
        📈 {team} currently has the strongest average momentum
        with a momentum score of {round(score,2)}.
        """

    # =========================
    # PRESSURE PLAYER
    # =========================

    elif "pressure" in q:

        player = (
            df.groupby("batter")["pressure_score"]
            .mean()
            .sort_values(ascending=False)
            .index[0]
        )

        score = (
            df.groupby("batter")["pressure_score"]
            .mean()
            .sort_values(ascending=False)
            .iloc[0]
        )

        answer = f"""
        ⚠️ {player} experiences the highest average pressure score
        of {round(score,2)} in MomentumX analytics.
        """

    # =========================
    # IMPACT PLAYER
    # =========================

    elif "impact" in q:

        player = (
            df.groupby("batter")["impact_score"]
            .mean()
            .sort_values(ascending=False)
            .index[0]
        )

        score = (
            df.groupby("batter")["impact_score"]
            .mean()
            .sort_values(ascending=False)
            .iloc[0]
        )

        answer = f"""
        🌟 {player} has the highest average impact score
        of {round(score,2)}.
        """

    # =========================
    # COLLAPSE RISK
    # =========================

    elif "collapse" in q:

        team = (
            df.groupby("inning_team")["pressure_score"]
            .mean()
            .sort_values(ascending=False)
            .index[0]
        )

        answer = f"""
        📉 {team} shows the highest collapse-risk tendencies
        according to pressure analytics.
        """

    # =========================
    # DEATH OVER
    # =========================

    elif "death" in q:

        death_df = df[df["phase"] == "Death Overs"]

        player = (
            death_df.groupby("batter")["batsman_runs"]
            .sum()
            .sort_values(ascending=False)
            .index[0]
        )

        runs = (
            death_df.groupby("batter")["batsman_runs"]
            .sum()
            .sort_values(ascending=False)
            .iloc[0]
        )

        answer = f"""
        ⚡ {player} dominates the death overs
        with {int(runs)} runs in death-over phases.
        """

    st.markdown(f"""
    <div class="answer">
    {answer}
    </div>
    """, unsafe_allow_html=True)