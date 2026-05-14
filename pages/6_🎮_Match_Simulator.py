import streamlit as st
import random
import time

st.set_page_config(
    page_title="Match Simulator",
    page_icon="🎮",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background:
        radial-gradient(circle at top left, rgba(59,130,246,0.18), transparent 30%),
        radial-gradient(circle at bottom right, rgba(239,68,68,0.18), transparent 30%),
        linear-gradient(135deg, #020617, #111827, #000000);
    color: white;
}

.sim-card {
    padding: 30px;
    border-radius: 28px;
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.15);
    box-shadow: 0 20px 60px rgba(0,0,0,0.45);
}

.title {
    font-size: 52px;
    font-weight: 950;
    background: linear-gradient(90deg, #38bdf8, #facc15, #ef4444);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="title">🎮 AI Match Simulator</div>',
    unsafe_allow_html=True
)

st.caption(
    "Simulate live IPL match situations using MomentumX Intelligence"
)

teams = [
    "RCB",
    "CSK",
    "MI",
    "KKR",
    "SRH",
    "DC",
    "GT",
    "RR"
]

c1, c2 = st.columns(2)

with c1:
    team1 = st.selectbox(
        "Select Team 1",
        teams
    )

with c2:
    team2 = st.selectbox(
        "Select Team 2",
        teams,
        index=1
    )

overs = st.slider(
    "Current Over",
    1,
    20,
    15
)

score = st.slider(
    "Current Score",
    0,
    250,
    145
)

wickets = st.slider(
    "Wickets Lost",
    0,
    10,
    4
)

if st.button("Run AI Simulation"):

    with st.spinner("MomentumX AI analyzing match situation..."):

        time.sleep(2)

        pressure = random.choice([
            "Low Pressure",
            "Moderate Pressure",
            "High Pressure"
        ])

        momentum = random.choice([
            f"{team1} dominating momentum",
            f"{team2} fighting back",
            "Momentum evenly balanced"
        ])

        winner = random.choice([
            team1,
            team2
        ])

        collapse = random.choice([
            "Low Collapse Risk",
            "Moderate Collapse Risk",
            "High Collapse Risk"
        ])

        verdict = random.choice([
            "Death overs may completely change this match.",
            "Momentum swing expected within next 2 overs.",
            "Pressure phase likely to trigger wicket event.",
            "Batting side currently controlling acceleration phase.",
            "Fielding pressure increasing significantly."
        ])

    st.write("")

    x1, x2 = st.columns(2)

    with x1:
        st.markdown(f"""
        <div class="sim-card">
            <h2>🏆 Predicted Winning Side</h2>
            <h1>{winner}</h1>
        </div>
        """, unsafe_allow_html=True)

    with x2:
        st.markdown(f"""
        <div class="sim-card">
            <h2>📈 Match Momentum</h2>
            <h1>{momentum}</h1>
        </div>
        """, unsafe_allow_html=True)

    st.write("")

    y1, y2 = st.columns(2)

    with y1:
        st.markdown(f"""
        <div class="sim-card">
            <h2>⚠️ Pressure Status</h2>
            <h1>{pressure}</h1>
        </div>
        """, unsafe_allow_html=True)

    with y2:
        st.markdown(f"""
        <div class="sim-card">
            <h2>📉 Collapse Risk</h2>
            <h1>{collapse}</h1>
        </div>
        """, unsafe_allow_html=True)

    st.write("")

    st.markdown(f"""
    <div class="sim-card">
        <h2>🧠 AI Match Verdict</h2>

        <p style="font-size:20px;">
        {verdict}
        </p>
    </div>
    """, unsafe_allow_html=True)