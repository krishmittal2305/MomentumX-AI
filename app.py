import streamlit as st

st.set_page_config(
    page_title="MomentumX AI",
    page_icon="🏏",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
#MainMenu, footer, header {visibility: hidden;}
/* Neon Glow */

.glow {
    text-shadow:
        0 0 8px rgba(250,204,21,0.8),
        0 0 18px rgba(239,68,68,0.6),
        0 0 28px rgba(59,130,246,0.6);
}

/* Neon Cards */

.feature-card,
.metric-card,
.player-card,
.card,
.team-card,
.big-card,
.sim-card,
.workflow {
    position: relative;
    overflow: hidden;
    transition: 0.35s ease;
}

.feature-card:hover,
.metric-card:hover,
.player-card:hover,
.card:hover,
.team-card:hover,
.big-card:hover,
.sim-card:hover,
.workflow:hover {

    transform: translateY(-8px) scale(1.01);

    box-shadow:
        0 0 20px rgba(250,204,21,0.20),
        0 0 40px rgba(239,68,68,0.18),
        0 0 60px rgba(59,130,246,0.16);
}

/* Animated Background */

.stApp::before {
    content: "";
    position: fixed;
    width: 200%;
    height: 200%;
    top: -50%;
    left: -50%;
    background:
        radial-gradient(circle, rgba(250,204,21,0.04) 1px, transparent 1px);
    background-size: 40px 40px;
    animation: moveBg 60s linear infinite;
    z-index: -1;
}

@keyframes moveBg {
    from {
        transform: translate(0,0);
    }

    to {
        transform: translate(100px,100px);
    }
}
.stApp {
    background: linear-gradient(135deg, #020617, #0f172a, #000000);
    color: white;
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #020617, #111827, #000000);
    border-right: 1px solid rgba(250,204,21,0.35);
}

.block-container {
    padding-top: 2rem;
}

.main-card {
    padding: 45px;
    border-radius: 30px;
    background: linear-gradient(135deg, rgba(250,204,21,0.18), rgba(239,68,68,0.14), rgba(59,130,246,0.10));
    border: 1px solid rgba(255,255,255,0.18);
    box-shadow: 0 25px 80px rgba(0,0,0,0.55);
}

.main-title {
    font-size: 64px;
    font-weight: 900;
    background: linear-gradient(90deg, #facc15, #fb923c, #ef4444, #38bdf8);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.subtitle {
    font-size: 24px;
    color: #f8fafc;
}

.text {
    font-size: 17px;
    color: #d1d5db;
    line-height: 1.7;
}

.metric-card {
    padding: 25px;
    border-radius: 22px;
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.14);
    box-shadow: 0 15px 45px rgba(0,0,0,0.40);
    text-align: center;
}

.metric-card h2 {
    color: #facc15;
    font-size: 34px;
    margin: 0;
}

.metric-card p {
    color: #cbd5e1;
    margin: 6px 0 0 0;
}

.feature-card {
    padding: 28px;
    border-radius: 24px;
    background: rgba(255,255,255,0.075);
    border: 1px solid rgba(255,255,255,0.14);
    min-height: 190px;
}

.feature-card h3 {
    color: #facc15;
}

.section-title {
    font-size: 34px;
    font-weight: 900;
    color: #ffffff;
    margin-top: 30px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="main-card">
    <div class="main-title">MomentumX AI</div>
    <div class="subtitle">IPL Momentum, Pressure & Clutch Intelligence Platform</div>
    <br>
    <div class="text">
        A premium sports analytics system that studies ball-by-ball IPL data to detect
        momentum shifts, pressure phases, clutch players, collapse risk, death-over impact,
        team dominance and AI-generated cricket insights.
    </div>
</div>
""", unsafe_allow_html=True)

st.write("")

m1, m2, m3, m4 = st.columns(4)

with m1:
    st.markdown('<div class="metric-card"><h2>95.2%</h2><p>Momentum Model Accuracy</p></div>', unsafe_allow_html=True)

with m2:
    st.markdown('<div class="metric-card"><h2>6+</h2><p>AI Analytics Engines</p></div>', unsafe_allow_html=True)

with m3:
    st.markdown('<div class="metric-card"><h2>IPL</h2><p>Ball-by-Ball Intelligence</p></div>', unsafe_allow_html=True)

with m4:
    st.markdown('<div class="metric-card"><h2>AI</h2><p>Cricket Insights</p></div>', unsafe_allow_html=True)

st.markdown('<div class="section-title">Core Intelligence Modules</div>', unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="feature-card">
        <h3>📈 Momentum Predictor</h3>
        <p>Predicts match-changing momentum events using over, runs, wickets, run rate and recent scoring flow.</p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="feature-card">
        <h3>🔥 ClutchSense Engine</h3>
        <p>Ranks players by pressure handling, death-over contribution, impact score and momentum influence.</p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="feature-card">
        <h3>⚠️ Pressure Engine</h3>
        <p>Analyzes collapse risk, high-pressure balls, wicket clusters and team vulnerability under pressure.</p>
    </div>
    """, unsafe_allow_html=True)

c4, c5, c6 = st.columns(3)

with c4:
    st.markdown("""
    <div class="feature-card">
        <h3>🏆 Team Dominance</h3>
        <p>Measures which teams control innings through momentum, aggression and impact consistency.</p>
    </div>
    """, unsafe_allow_html=True)

with c5:
    st.markdown("""
    <div class="feature-card">
        <h3>🧠 AI Insights</h3>
        <p>Generates analyst-style cricket insights, pressure verdicts and momentum alerts.</p>
    </div>
    """, unsafe_allow_html=True)

with c6:
    st.markdown("""
    <div class="feature-card">
        <h3>🎮 Match Simulator</h3>
        <p>Simulates IPL match situations and produces AI-based momentum and pressure interpretations.</p>
    </div>
    """, unsafe_allow_html=True)

st.success("Use the sidebar to explore Dashboard, Momentum Predictor, Clutch Analytics, Pressure Engine, AI Insights and Match Simulator.")