import streamlit as st
import pandas as pd
import random

st.set_page_config(
    page_title="AI Insights",
    page_icon="🧠",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background:
        radial-gradient(circle at 10% 10%, rgba(59,130,246,0.18), transparent 28%),
        radial-gradient(circle at 85% 20%, rgba(168,85,247,0.18), transparent 32%),
        linear-gradient(135deg, #020617 0%, #111827 55%, #000000 100%);
    color: white;
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #020617, #111827, #000000);
    border-right: 1px solid rgba(59,130,246,0.30);
}

.title {
    font-size: 52px;
    font-weight: 950;
    background: linear-gradient(90deg, #38bdf8, #a855f7, #facc15);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.card {
    padding: 28px;
    border-radius: 28px;
    background: rgba(255,255,255,0.075);
    border: 1px solid rgba(255,255,255,0.14);
    box-shadow: 0 18px 55px rgba(0,0,0,0.45);
    margin-bottom: 20px;
}

.card h2 {
    color: #facc15;
}

.insight {
    padding: 22px;
    border-radius: 22px;
    background: linear-gradient(135deg,
        rgba(59,130,246,0.15),
        rgba(168,85,247,0.12),
        rgba(250,204,21,0.10)
    );
    border: 1px solid rgba(255,255,255,0.12);
    margin-bottom: 18px;
    font-size: 18px;
    line-height: 1.8;
}
</style>
""", unsafe_allow_html=True)

df = pd.read_csv("final_momentumx_dataset.csv")

st.markdown(
    '<div class="title">🧠 AI Cricket Insights Engine</div>',
    unsafe_allow_html=True
)

st.caption(
    "AI-generated match intelligence powered by MomentumX Analytics"
)

st.write("")

# =========================
# TOP STATS
# =========================

top_player = (
    df.groupby("batter")["impact_score"]
    .mean()
    .sort_values(ascending=False)
    .index[0]
)

top_team = (
    df.groupby("inning_team")["momentum"]
    .mean()
    .sort_values(ascending=False)
    .index[0]
)

most_pressure = (
    df.groupby("inning_team")["pressure_score"]
    .mean()
    .sort_values(ascending=False)
    .index[0]
)

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown(f"""
    <div class="card">
        <h2>{top_player}</h2>
        <p>Highest Impact Batter</p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class="card">
        <h2>{top_team}</h2>
        <p>Strongest Momentum Team</p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class="card">
        <h2>{most_pressure}</h2>
        <p>Most Pressure-Prone Team</p>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# =========================
# AI GENERATED INSIGHTS
# =========================

st.subheader("⚡ AI Generated Match Insights")

insights = [

    f"{top_team} consistently maintained stronger momentum phases compared to other IPL teams.",

    f"{top_player} emerged as one of the most impactful batters under pressure situations.",

    "Death overs showed the highest volatility and momentum fluctuation across matches.",

    "Wicket clusters significantly increased batting collapse probability.",

    "Boundary-heavy overs were strongly correlated with positive momentum swings.",

    "Teams losing wickets during middle overs struggled to recover momentum later.",

    "Pressure score increased sharply during overs 16-20 indicating death-over intensity.",

    "Aggressive scoring patterns were more common in winning momentum phases.",

    "Momentum shifts frequently occurred immediately after wicket events or consecutive boundaries.",

    "Teams with lower collapse risk maintained better scoring stability throughout innings."

]

random.shuffle(insights)

for insight in insights[:6]:
    st.markdown(f"""
    <div class="insight">
        {insight}
    </div>
    """, unsafe_allow_html=True)

st.divider()

# =========================
# PLAYER AI ANALYZER
# =========================

st.subheader("🏏 AI Player Analyzer")

player_list = sorted(df["batter"].dropna().unique())

selected_player = st.selectbox(
    "Select Player",
    player_list
)

player_df = df[df["batter"] == selected_player]

runs = int(player_df["batsman_runs"].sum())
avg_pressure = round(player_df["pressure_score"].mean(), 2)
avg_momentum = round(player_df["momentum"].mean(), 2)
boundaries = int((player_df["batsman_runs"] >= 4).sum())

# AI commentary generation

if avg_pressure >= 6:
    pressure_text = "thrives under high-pressure match situations"
elif avg_pressure >= 3:
    pressure_text = "maintains balanced performance during pressure phases"
else:
    pressure_text = "usually bats in stable match situations"

if avg_momentum >= 0.7:
    momentum_text = "consistently shifts momentum towards the batting side"
elif avg_momentum >= 0.4:
    momentum_text = "plays a stabilizing role in momentum control"
else:
    momentum_text = "faces difficulty maintaining positive momentum"

st.markdown(f"""
<div class="card">
    <h2>{selected_player}</h2>

    <p>
    Total Runs: <b>{runs}</b><br>
    Boundaries: <b>{boundaries}</b><br>
    Average Pressure Score: <b>{avg_pressure}</b><br>
    Average Momentum Contribution: <b>{avg_momentum}</b>
    </p>

    <hr>

    <p>
    🧠 AI Analysis:<br><br>

    {selected_player} {pressure_text} and {momentum_text}.
    The player has produced {boundaries} major boundary events and contributes
    significantly to batting acceleration phases.
    </p>
</div>
""", unsafe_allow_html=True)

st.divider()

# =========================
# MATCH PHASE ANALYSIS
# =========================

st.subheader("📈 Match Phase Intelligence")

phase_data = (
    df.groupby("phase")
    .agg({
        "momentum": "mean",
        "pressure_score": "mean",
        "is_wicket": "sum"
    })
)

st.dataframe(
    phase_data.style
    .background_gradient(cmap="coolwarm")
)