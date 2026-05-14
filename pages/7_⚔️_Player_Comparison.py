import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(
    page_title="Player Comparison",
    page_icon="⚔️",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background:
        radial-gradient(circle at 10% 10%, rgba(250,204,21,0.18), transparent 30%),
        radial-gradient(circle at 85% 25%, rgba(239,68,68,0.20), transparent 32%),
        linear-gradient(135deg, #020617, #0f172a, #000000);
    color: white;
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #020617, #111827, #000000);
    border-right: 1px solid rgba(250,204,21,0.30);
}

.title {
    font-size: 48px;
    font-weight: 950;
    background: linear-gradient(90deg, #facc15, #fb923c, #ef4444);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.card {
    padding: 25px;
    border-radius: 24px;
    background: rgba(255,255,255,0.075);
    border: 1px solid rgba(255,255,255,0.14);
    box-shadow: 0 18px 55px rgba(0,0,0,0.45);
    text-align: center;
}

.card h2 {
    color: #facc15;
    font-size: 32px;
}

.verdict {
    padding: 28px;
    border-radius: 28px;
    background: linear-gradient(135deg, rgba(250,204,21,0.16), rgba(239,68,68,0.12));
    border: 1px solid rgba(250,204,21,0.25);
    box-shadow: 0 18px 55px rgba(0,0,0,0.45);
    font-size: 18px;
    line-height: 1.8;
}
</style>
""", unsafe_allow_html=True)

df = pd.read_csv("final_momentumx_dataset.csv")

st.markdown('<div class="title">⚔️ Player vs Player AI Comparison</div>', unsafe_allow_html=True)
st.caption("Compare IPL players using impact, pressure, momentum and scoring intelligence.")

players = sorted(df["batter"].dropna().unique())

col1, col2 = st.columns(2)

with col1:
    player1 = st.selectbox("Select Player 1", players)

with col2:
    player2 = st.selectbox("Select Player 2", players, index=1)

def player_stats(player):
    p = df[df["batter"] == player]

    return {
        "Runs": int(p["batsman_runs"].sum()),
        "Balls": len(p),
        "Boundaries": int((p["batsman_runs"] >= 4).sum()),
        "Impact": round(p["impact_score"].mean(), 2),
        "Pressure": round(p["pressure_score"].mean(), 2),
        "Momentum": round(p["momentum"].mean(), 2),
    }

s1 = player_stats(player1)
s2 = player_stats(player2)

st.divider()

a, b = st.columns(2)

with a:
    st.markdown(f"""
    <div class="card">
        <h2>{player1}</h2>
        <p>Runs: <b>{s1["Runs"]}</b></p>
        <p>Boundaries: <b>{s1["Boundaries"]}</b></p>
        <p>Impact Score: <b>{s1["Impact"]}</b></p>
        <p>Pressure Score: <b>{s1["Pressure"]}</b></p>
        <p>Momentum: <b>{s1["Momentum"]}</b></p>
    </div>
    """, unsafe_allow_html=True)

with b:
    st.markdown(f"""
    <div class="card">
        <h2>{player2}</h2>
        <p>Runs: <b>{s2["Runs"]}</b></p>
        <p>Boundaries: <b>{s2["Boundaries"]}</b></p>
        <p>Impact Score: <b>{s2["Impact"]}</b></p>
        <p>Pressure Score: <b>{s2["Pressure"]}</b></p>
        <p>Momentum: <b>{s2["Momentum"]}</b></p>
    </div>
    """, unsafe_allow_html=True)

st.divider()

categories = ["Runs", "Boundaries", "Impact", "Pressure", "Momentum"]

values1 = [
    s1["Runs"] / max(s1["Runs"], s2["Runs"], 1) * 100,
    s1["Boundaries"] / max(s1["Boundaries"], s2["Boundaries"], 1) * 100,
    s1["Impact"] / max(s1["Impact"], s2["Impact"], 1) * 100,
    s1["Pressure"] / max(s1["Pressure"], s2["Pressure"], 1) * 100,
    s1["Momentum"] / max(s1["Momentum"], s2["Momentum"], 1) * 100,
]

values2 = [
    s2["Runs"] / max(s1["Runs"], s2["Runs"], 1) * 100,
    s2["Boundaries"] / max(s1["Boundaries"], s2["Boundaries"], 1) * 100,
    s2["Impact"] / max(s1["Impact"], s2["Impact"], 1) * 100,
    s2["Pressure"] / max(s1["Pressure"], s2["Pressure"], 1) * 100,
    s2["Momentum"] / max(s1["Momentum"], s2["Momentum"], 1) * 100,
]

fig = go.Figure()

fig.add_trace(go.Scatterpolar(
    r=values1,
    theta=categories,
    fill="toself",
    name=player1
))

fig.add_trace(go.Scatterpolar(
    r=values2,
    theta=categories,
    fill="toself",
    name=player2
))

fig.update_layout(
    template="plotly_dark",
    polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
    height=600,
    title="AI Radar Comparison"
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

score1 = s1["Impact"] + s1["Momentum"] + (s1["Runs"] / 100)
score2 = s2["Impact"] + s2["Momentum"] + (s2["Runs"] / 100)

winner = player1 if score1 > score2 else player2

st.markdown(f"""
<div class="verdict">
    <h2>🧠 AI Verdict: {winner} has stronger overall MomentumX profile</h2>
    <p>
    The comparison is based on scoring volume, boundary creation, pressure handling,
    impact score and momentum contribution. This does not only compare runs — it compares
    how much influence the player creates in match situations.
    </p>
</div>
""", unsafe_allow_html=True)