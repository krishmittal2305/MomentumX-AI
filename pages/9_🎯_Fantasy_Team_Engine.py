import streamlit as st
import pandas as pd
import plotly.express as px
import random

st.set_page_config(
    page_title="Fantasy Team Engine",
    page_icon="🎯",
    layout="wide"
)

st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(circle at top left, rgba(250,204,21,0.18), transparent 30%),
        radial-gradient(circle at top right, rgba(239,68,68,0.18), transparent 32%),
        linear-gradient(135deg, #020617, #111827, #000000);
    color: white;
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #020617, #111827, #000000);
}

.title {
    font-size: 52px;
    font-weight: 950;
    background: linear-gradient(90deg, #facc15, #fb923c, #ef4444);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.card {
    padding: 24px;
    border-radius: 24px;
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.15);
    box-shadow: 0 18px 55px rgba(0,0,0,0.45);
    margin-bottom: 20px;
}

.card h2 {
    color: #facc15;
}

.pick {
    padding: 18px;
    border-radius: 18px;
    background: linear-gradient(135deg,
        rgba(250,204,21,0.15),
        rgba(239,68,68,0.10));
    border: 1px solid rgba(255,255,255,0.12);
    margin-bottom: 12px;
    font-size: 18px;
}

</style>
""", unsafe_allow_html=True)

df = pd.read_csv("final_momentumx_dataset.csv")

st.markdown(
    '<div class="title">🎯 Fantasy Team Recommendation Engine</div>',
    unsafe_allow_html=True
)

st.caption(
    "AI-powered IPL fantasy recommendations using MomentumX analytics."
)

# =========================
# PLAYER ANALYTICS
# =========================

fantasy = (
    df.groupby("batter")
    .agg({
        "batsman_runs": "sum",
        "impact_score": "mean",
        "momentum": "mean",
        "pressure_score": "mean"
    })
    .reset_index()
)

fantasy["fantasy_score"] = (
    fantasy["batsman_runs"] * 0.4 +
    fantasy["impact_score"] * 120 +
    fantasy["momentum"] * 160 -
    fantasy["pressure_score"] * 18
)

fantasy = fantasy.sort_values(
    by="fantasy_score",
    ascending=False
)

top_team = fantasy.head(11)

captain = top_team.iloc[0]["batter"]
vice_captain = top_team.iloc[1]["batter"]

safe_pick = top_team.iloc[2]["batter"]

risky_pick = fantasy.sample(1).iloc[0]["batter"]

st.divider()

# =========================
# CAPTAIN SECTION
# =========================

c1, c2 = st.columns(2)

with c1:
    st.markdown(f"""
    <div class="card">
        <h2>👑 Captain Pick</h2>
        <h1>{captain}</h1>

        <p>
        Highest overall fantasy intelligence score.
        </p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class="card">
        <h2>⭐ Vice Captain Pick</h2>
        <h1>{vice_captain}</h1>

        <p>
        Strong momentum and clutch contribution.
        </p>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# =========================
# TOP XI
# =========================

st.subheader("🏏 AI Fantasy XI")

cols = st.columns(3)

for i, (_, row) in enumerate(top_team.iterrows()):

    with cols[i % 3]:

        st.markdown(f"""
        <div class="pick">
            <b>{row['batter']}</b><br>
            Fantasy Score: {round(row['fantasy_score'],2)}
        </div>
        """, unsafe_allow_html=True)

st.divider()

# =========================
# SPECIAL PICKS
# =========================

a, b = st.columns(2)

with a:
    st.markdown(f"""
    <div class="card">
        <h2>🛡️ Safe Pick</h2>
        <h1>{safe_pick}</h1>

        <p>
        Consistent performer with reliable scoring output.
        </p>
    </div>
    """, unsafe_allow_html=True)

with b:
    st.markdown(f"""
    <div class="card">
        <h2>🔥 Differential Pick</h2>
        <h1>{risky_pick}</h1>

        <p>
        High-risk high-reward player capable of surprise impact.
        </p>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# =========================
# VISUALIZATION
# =========================

st.subheader("📈 Fantasy Score Distribution")

fig = px.bar(
    top_team,
    x="batter",
    y="fantasy_score",
    color="fantasy_score",
    template="plotly_dark",
    color_continuous_scale="Plasma"
)

fig.update_layout(
    height=550,
    xaxis_title="Players",
    yaxis_title="Fantasy Score"
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

# =========================
# AI VERDICT
# =========================

verdicts = [

    "Momentum-heavy players dominate fantasy projections this season.",

    "Death-over impact significantly boosts fantasy intelligence scores.",

    "Players with lower pressure scores tend to provide stable fantasy returns.",

    "Boundary acceleration strongly influences fantasy prediction quality.",

    "MomentumX AI prioritizes match influence over raw scoring volume."

]

st.subheader("🧠 AI Fantasy Verdict")

st.markdown(f"""
<div class="card">
    <p style="font-size:20px; line-height:1.8;">
    {random.choice(verdicts)}
    </p>
</div>
""", unsafe_allow_html=True)