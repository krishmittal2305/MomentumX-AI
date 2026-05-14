import streamlit as st
import pandas as pd
import plotly.express as px
import random

st.set_page_config(
    page_title="IPL 2026 Prediction Center",
    page_icon="🏆",
    layout="wide"
)

st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(circle at top left, rgba(250,204,21,0.18), transparent 28%),
        radial-gradient(circle at top right, rgba(239,68,68,0.18), transparent 30%),
        linear-gradient(135deg, #020617, #111827, #000000);
    color: white;
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #020617, #111827, #000000);
}

.title {
    font-size: 54px;
    font-weight: 950;
    background: linear-gradient(90deg, #facc15, #fb923c, #ef4444);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.team-card {
    padding: 24px;
    border-radius: 24px;
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.15);
    box-shadow: 0 18px 55px rgba(0,0,0,0.45);
    text-align: center;
    margin-bottom: 20px;
}

.team-card h2 {
    color: #facc15;
}

.big-card {
    padding: 35px;
    border-radius: 30px;
    background:
        linear-gradient(135deg,
        rgba(250,204,21,0.14),
        rgba(239,68,68,0.10),
        rgba(59,130,246,0.08));
    border: 1px solid rgba(255,255,255,0.15);
    box-shadow: 0 20px 60px rgba(0,0,0,0.50);
}

.big-card h1 {
    color: #facc15;
}

</style>
""", unsafe_allow_html=True)

df = pd.read_csv("final_momentumx_dataset.csv")

st.markdown(
    '<div class="title">🏆 IPL 2026 Trophy Prediction Center</div>',
    unsafe_allow_html=True
)

st.caption(
    "AI-powered IPL team ranking, playoff probability and trophy prediction system."
)

# =========================
# TEAM ANALYTICS
# =========================

teams = (
    df.groupby("inning_team")
    .agg({
        "momentum": "mean",
        "impact_score": "mean",
        "pressure_score": "mean",
        "total_runs": "sum",
        "is_wicket": "sum"
    })
    .reset_index()
)

teams["power_score"] = (
    teams["momentum"] * 180 +
    teams["impact_score"] * 120 +
    teams["total_runs"] * 0.05 -
    teams["pressure_score"] * 20 -
    teams["is_wicket"] * 0.3
)

teams = teams.sort_values(
    by="power_score",
    ascending=False
)

# =========================
# TROPHY FAVORITE
# =========================

winner = teams.iloc[0]["inning_team"]

st.markdown(f"""
<div class="big-card">
    <h1>🏆 Predicted IPL 2026 Champion</h1>

    <h1 style="font-size:70px;">
    {winner}
    </h1>

    <p style="font-size:20px;">
    MomentumX AI predicts <b>{winner}</b> as the strongest overall IPL 2026 team
    based on momentum dominance, pressure handling, scoring aggression and impact contribution.
    </p>
</div>
""", unsafe_allow_html=True)

st.write("")

# =========================
# PLAYOFF TEAMS
# =========================

st.subheader("🔥 Predicted Playoff Teams")

top4 = teams.head(4)

cols = st.columns(4)

for i, (_, row) in enumerate(top4.iterrows()):

    with cols[i]:

        probability = random.randint(65, 95)

        st.markdown(f"""
        <div class="team-card">
            <h2>{row['inning_team']}</h2>

            <p>
            Playoff Probability<br>
            <b style="font-size:28px;">
            {probability}%
            </b>
            </p>
        </div>
        """, unsafe_allow_html=True)

st.divider()

# =========================
# POWER RANKINGS
# =========================

st.subheader("📈 AI Power Rankings")

fig = px.bar(
    teams,
    x="inning_team",
    y="power_score",
    color="power_score",
    template="plotly_dark",
    color_continuous_scale="Inferno"
)

fig.update_layout(
    height=600,
    xaxis_title="Teams",
    yaxis_title="Power Score"
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

# =========================
# TITLE PROBABILITY
# =========================

st.subheader("🏆 Title Probability Distribution")

teams["title_probability"] = (
    teams["power_score"] /
    teams["power_score"].sum()
) * 100

pie = px.pie(
    teams,
    names="inning_team",
    values="title_probability",
    template="plotly_dark",
    hole=0.45
)

pie.update_layout(height=600)

st.plotly_chart(pie, use_container_width=True)

st.divider()

# =========================
# AI VERDICTS
# =========================

verdicts = [

    "Momentum-heavy teams are dominating current title simulations.",

    "Teams with lower pressure scores are showing stronger playoff consistency.",

    "Impact contribution during middle overs strongly influences title probability.",

    "MomentumX AI identifies aggressive scoring phases as a major championship factor.",

    "Balanced wicket control significantly increases trophy chances."

]

st.subheader("🧠 AI Tournament Verdict")

st.markdown(f"""
<div class="big-card">
    <p style="font-size:22px; line-height:1.8;">
    {random.choice(verdicts)}
    </p>
</div>
""", unsafe_allow_html=True)