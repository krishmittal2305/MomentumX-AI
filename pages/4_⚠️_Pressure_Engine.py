import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Pressure Engine", page_icon="⚠️", layout="wide")

st.markdown("""
<style>
.stApp {
    background:
        radial-gradient(circle at 15% 15%, rgba(239,68,68,0.20), transparent 30%),
        radial-gradient(circle at 85% 20%, rgba(250,204,21,0.16), transparent 30%),
        linear-gradient(135deg, #020617, #111827 55%, #000000);
    color: white;
}
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #020617, #111827, #000000);
    border-right: 1px solid rgba(239,68,68,0.30);
}
.title {
    font-size: 48px;
    font-weight: 950;
    background: linear-gradient(90deg, #ef4444, #fb923c, #facc15);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.card {
    padding: 25px;
    border-radius: 26px;
    background: rgba(255,255,255,0.075);
    border: 1px solid rgba(255,255,255,0.14);
    box-shadow: 0 18px 50px rgba(0,0,0,0.45);
    text-align: center;
}
.card h2 {
    color: #facc15;
    font-size: 34px;
}
.card p {
    color: #cbd5e1;
}
</style>
""", unsafe_allow_html=True)

df = pd.read_csv("final_momentumx_dataset.csv")
collapse = pd.read_csv("collapse_risk.csv")

# Fix team column safely
if "team" not in collapse.columns:
    first_col = collapse.columns[0]
    collapse = collapse.rename(columns={first_col: "team"})

st.markdown('<div class="title">⚠️ Pressure Engine</div>', unsafe_allow_html=True)
st.caption("Analyze pressure phases, collapse risk, wicket pressure and team vulnerability.")

st.write("")

avg_pressure = round(df["pressure_score"].mean(), 2)
high_pressure_balls = len(df[df["pressure_score"] >= 5])
total_wickets = int(df["is_wicket"].sum())
most_risky_team = collapse.iloc[0]["team"]

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(f'<div class="card"><h2>{avg_pressure}</h2><p>Average Pressure Score</p></div>', unsafe_allow_html=True)

with c2:
    st.markdown(f'<div class="card"><h2>{high_pressure_balls:,}</h2><p>High Pressure Balls</p></div>', unsafe_allow_html=True)

with c3:
    st.markdown(f'<div class="card"><h2>{total_wickets:,}</h2><p>Total Wickets</p></div>', unsafe_allow_html=True)

with c4:
    st.markdown(f'<div class="card"><h2>{most_risky_team}</h2><p>Highest Collapse Risk</p></div>', unsafe_allow_html=True)

st.divider()

left, right = st.columns(2)

with left:
    st.subheader("🔥 Pressure by Match Phase")
    phase_pressure = df.groupby("phase")["pressure_score"].mean().reset_index()

    fig = px.bar(
        phase_pressure,
        x="phase",
        y="pressure_score",
        template="plotly_dark",
        color="pressure_score",
        color_continuous_scale="Reds"
    )
    fig.update_layout(height=450)
    st.plotly_chart(fig, use_container_width=True)

with right:
    st.subheader("⚠️ Team Collapse Risk")
    fig = px.bar(
        collapse.head(10),
        x="collapse_risk",
        y="team",
        orientation="h",
        template="plotly_dark",
        color="collapse_risk",
        color_continuous_scale="Reds"
    )
    fig.update_layout(height=450, yaxis=dict(autorange="reversed"))
    st.plotly_chart(fig, use_container_width=True)

st.divider()

st.subheader("📉 Wicket Pressure Timeline")

wicket_over = df.groupby("over")["is_wicket"].sum().reset_index()

fig = px.line(
    wicket_over,
    x="over",
    y="is_wicket",
    markers=True,
    template="plotly_dark"
)

fig.update_traces(line=dict(width=4))
fig.update_layout(height=450, xaxis_title="Over", yaxis_title="Wickets")

st.plotly_chart(fig, use_container_width=True)

st.divider()

st.subheader("🧠 Pressure Insight")

selected_team = st.selectbox("Select Team", sorted(df["inning_team"].dropna().unique()))
team_df = df[df["inning_team"] == selected_team]

team_pressure = round(team_df["pressure_score"].mean(), 2)
team_wickets = int(team_df["is_wicket"].sum())
team_dot_balls = int((team_df["total_runs"] == 0).sum())

st.markdown(f"""
<div class="card">
    <h2>{selected_team}</h2>
    <p>
    Average pressure score: <b>{team_pressure}</b><br>
    Total wickets lost: <b>{team_wickets}</b><br>
    Dot balls faced: <b>{team_dot_balls}</b><br><br>
    MomentumX interprets this as a measure of how often the team enters uncomfortable
    match situations and how vulnerable it is to collapse under pressure.
    </p>
</div>
""", unsafe_allow_html=True)