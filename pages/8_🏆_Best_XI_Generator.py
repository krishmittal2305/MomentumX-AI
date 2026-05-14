import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Best XI Generator",
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
    font-size: 52px;
    font-weight: 950;
    background: linear-gradient(90deg, #facc15, #fb923c, #ef4444);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.player-card {
    padding: 22px;
    border-radius: 22px;
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.15);
    box-shadow: 0 18px 55px rgba(0,0,0,0.45);
    text-align: center;
    margin-bottom: 20px;
}

.player-card h2 {
    color: #facc15;
    font-size: 28px;
}

.player-card p {
    color: #cbd5e1;
}

.team-box {
    padding: 35px;
    border-radius: 30px;
    background:
        linear-gradient(135deg,
        rgba(250,204,21,0.15),
        rgba(239,68,68,0.10),
        rgba(59,130,246,0.08));
    border: 1px solid rgba(255,255,255,0.15);
    box-shadow: 0 20px 60px rgba(0,0,0,0.50);
}

.team-box h2 {
    color: #facc15;
}

</style>
""", unsafe_allow_html=True)

df = pd.read_csv("final_momentumx_dataset.csv")

st.markdown(
    '<div class="title">🏆 AI Best XI Generator</div>',
    unsafe_allow_html=True
)

st.caption(
    "Generate the strongest IPL playing XI using MomentumX Intelligence."
)

# =========================
# PLAYER SCORING ENGINE
# =========================

player_stats = (
    df.groupby("batter")
    .agg({
        "batsman_runs": "sum",
        "impact_score": "mean",
        "momentum": "mean",
        "pressure_score": "mean"
    })
    .reset_index()
)

player_stats["ai_score"] = (
    player_stats["batsman_runs"] * 0.35 +
    player_stats["impact_score"] * 120 +
    player_stats["momentum"] * 180 -
    player_stats["pressure_score"] * 20
)

player_stats = player_stats.sort_values(
    by="ai_score",
    ascending=False
)

best_xi = player_stats.head(11)

st.write("")

st.markdown("""
<div class="team-box">
    <h2>🧠 MomentumX AI Selected Playing XI</h2>
    <p>
    This XI is generated using impact score, momentum contribution,
    scoring consistency and pressure handling.
    </p>
</div>
""", unsafe_allow_html=True)

st.write("")

# =========================
# DISPLAY PLAYERS
# =========================

cols = st.columns(3)

for i, (_, row) in enumerate(best_xi.iterrows()):

    with cols[i % 3]:

        st.markdown(f"""
        <div class="player-card">
            <h2>{row['batter']}</h2>

            <p>
            Runs: <b>{int(row['batsman_runs'])}</b><br>
            Impact: <b>{round(row['impact_score'],2)}</b><br>
            Momentum: <b>{round(row['momentum'],2)}</b><br>
            AI Score: <b>{round(row['ai_score'],2)}</b>
            </p>
        </div>
        """, unsafe_allow_html=True)

st.divider()

# =========================
# BEST PLAYER
# =========================

best_player = best_xi.iloc[0]

st.markdown(f"""
<div class="team-box">
    <h2>🌟 Captain Pick: {best_player['batter']}</h2>

    <p>
    MomentumX AI selected <b>{best_player['batter']}</b> as the strongest
    overall player based on impact score, momentum contribution and scoring output.
    </p>
</div>
""", unsafe_allow_html=True)

st.divider()

# =========================
# VISUALIZATION
# =========================

st.subheader("📈 AI Score Distribution")

fig = px.bar(
    best_xi,
    x="batter",
    y="ai_score",
    color="ai_score",
    template="plotly_dark",
    color_continuous_scale="Inferno"
)

fig.update_layout(
    height=550,
    xaxis_title="Players",
    yaxis_title="AI Score"
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

# =========================
# ROLE ANALYSIS
# =========================

st.subheader("🎯 Team Role Intelligence")

roles = []

for _, row in best_xi.iterrows():

    if row["momentum"] > 1:
        role = "Match Accelerator"

    elif row["impact_score"] > 2:
        role = "Clutch Performer"

    else:
        role = "Stabilizer"

    roles.append(role)

best_xi["role"] = roles

role_fig = px.pie(
    best_xi,
    names="role",
    template="plotly_dark",
    hole=0.45
)

role_fig.update_layout(height=500)

st.plotly_chart(role_fig, use_container_width=True)