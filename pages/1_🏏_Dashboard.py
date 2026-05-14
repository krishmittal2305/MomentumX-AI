import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dashboard", layout="wide")

st.markdown("""
<style>
.stApp {
    background: radial-gradient(circle at top right, #111827, #020617 55%, #000000);
    color: white;
}

.big-title {
    font-size: 42px;
    font-weight: 900;
    background: linear-gradient(90deg, #facc15, #fb923c);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.info-card {
    padding: 24px;
    border-radius: 22px;
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.15);
    box-shadow: 0 10px 35px rgba(0,0,0,0.35);
}

.info-card h2 {
    color: #facc15;
    margin-bottom: 0;
}
</style>
""", unsafe_allow_html=True)

df = pd.read_csv("final_momentumx_dataset.csv")
clutch = pd.read_csv("clutch_players.csv")
death = pd.read_csv("death_players.csv")
team = pd.read_csv("team_momentum.csv")
collapse = pd.read_csv("collapse_risk.csv")

st.markdown('<div class="big-title">🏏 IPL Intelligence Dashboard</div>', unsafe_allow_html=True)
st.caption("Momentum, pressure, clutch performance and team dominance analytics")

st.write("")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class="info-card">
        <h2>{len(df):,}</h2>
        <p>Total Deliveries</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="info-card">
        <h2>{df['batter'].nunique()}</h2>
        <p>Players Analyzed</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="info-card">
        <h2>{df['inning_team'].nunique()}</h2>
        <p>Teams Covered</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="info-card">
        <h2>{round(df['pressure_score'].mean(), 2)}</h2>
        <p>Avg Pressure Score</p>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.divider()

c1, c2 = st.columns(2)

with c1:
    st.subheader("🔥 Top Clutch Players")
    fig = px.bar(
        clutch.head(10),
        x="clutch_index",
        y=clutch.head(10).iloc[:, 0],
        orientation="h",
        template="plotly_dark",
        color="clutch_index",
        color_continuous_scale="Inferno"
    )
    fig.update_layout(height=450, yaxis_title="Player", xaxis_title="Clutch Index")
    st.plotly_chart(fig, use_container_width=True)

with c2:
    st.subheader("⚡ Death Over Finishers")
    fig = px.bar(
        death.head(10),
        x="death_score",
        y=death.head(10).iloc[:, 0],
        orientation="h",
        template="plotly_dark",
        color="death_score",
        color_continuous_scale="Oranges"
    )
    fig.update_layout(height=450, yaxis_title="Player", xaxis_title="Death Score")
    st.plotly_chart(fig, use_container_width=True)

st.divider()

c3, c4 = st.columns(2)

with c3:
    st.subheader("🏆 Team Dominance")
    fig = px.bar(
        team.head(10),
        x="dominance_score",
        y=team.head(10).iloc[:, 0],
        orientation="h",
        template="plotly_dark",
        color="dominance_score",
        color_continuous_scale="Viridis"
    )
    fig.update_layout(height=450, yaxis_title="Team", xaxis_title="Dominance Score")
    st.plotly_chart(fig, use_container_width=True)

with c4:
    st.subheader("⚠️ Collapse Risk")
    fig = px.bar(
        collapse.head(10),
        x="collapse_risk",
        y=collapse.head(10).iloc[:, 0],
        orientation="h",
        template="plotly_dark",
        color="collapse_risk",
        color_continuous_scale="Reds"
    )
    fig.update_layout(height=450, yaxis_title="Team", xaxis_title="Collapse Risk")
    st.plotly_chart(fig, use_container_width=True)

st.divider()

st.subheader("📈 Momentum Timeline Across Overs")

momentum_over = df.groupby("over")["momentum"].mean().reset_index()

fig = px.line(
    momentum_over,
    x="over",
    y="momentum",
    template="plotly_dark",
    markers=True
)

fig.update_traces(line=dict(width=4))
fig.update_layout(height=450, xaxis_title="Over", yaxis_title="Average Momentum")

st.plotly_chart(fig, use_container_width=True)