import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Clutch Analytics", page_icon="🔥", layout="wide")

st.markdown("""
<style>
.stApp {
    background:
        radial-gradient(circle at 20% 10%, rgba(250,204,21,0.17), transparent 30%),
        radial-gradient(circle at 80% 30%, rgba(239,68,68,0.18), transparent 32%),
        linear-gradient(135deg, #020617, #0f172a 55%, #000000);
    color: white;
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #020617, #111827, #000000);
    border-right: 1px solid rgba(250,204,21,0.25);
}

.title {
    font-size: 48px;
    font-weight: 950;
    background: linear-gradient(90deg, #facc15, #fb923c, #ef4444);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.sub {
    color: #cbd5e1;
    font-size: 17px;
}

.kpi {
    padding: 24px;
    border-radius: 26px;
    background: rgba(255,255,255,0.075);
    border: 1px solid rgba(255,255,255,0.14);
    box-shadow: 0 18px 50px rgba(0,0,0,0.42);
    text-align: center;
}

.kpi h2 {
    color: #facc15;
    font-size: 34px;
    margin: 0;
}

.kpi p {
    color: #cbd5e1;
    margin: 0;
}

.player-card {
    padding: 28px;
    border-radius: 30px;
    background:
        linear-gradient(145deg, rgba(250,204,21,0.16), rgba(239,68,68,0.10), rgba(255,255,255,0.05));
    border: 1px solid rgba(250,204,21,0.25);
    box-shadow: 0 18px 55px rgba(0,0,0,0.45);
}

.player-card h2 {
    color: #facc15;
    font-size: 34px;
}

.player-card p {
    color: #e5e7eb;
}
</style>
""", unsafe_allow_html=True)

def load_index_csv(path, name_col="player"):
    data = pd.read_csv(path)

    if name_col not in data.columns:
        data = pd.read_csv(path, index_col=0).reset_index()
        data = data.rename(columns={"index": name_col})

    if name_col not in data.columns:
        data = data.rename(columns={data.columns[0]: name_col})

    return data

clutch = load_index_csv("clutch_players.csv", "player")
death = load_index_csv("death_players.csv", "player")
players = load_index_csv("player_intelligence.csv", "player")
df = pd.read_csv("final_momentumx_dataset.csv")

st.markdown('<div class="title">🔥 ClutchSense Analytics</div>', unsafe_allow_html=True)
st.markdown('<div class="sub">Discover pressure performers, death-over monsters and hidden IPL impact players.</div>', unsafe_allow_html=True)

st.write("")

top_clutch_name = clutch.iloc[0]["player"]
top_death_name = death.iloc[0]["player"]
top_player_name = players.iloc[0]["player"]

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown(f"""
    <div class="kpi">
        <h2>{top_clutch_name}</h2>
        <p>Top Clutch Player</p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class="kpi">
        <h2>{top_death_name}</h2>
        <p>Best Death Over Finisher</p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class="kpi">
        <h2>{top_player_name}</h2>
        <p>Highest AI Player Rating</p>
    </div>
    """, unsafe_allow_html=True)

st.divider()

left, right = st.columns(2)

with left:
    st.subheader("🔥 Top 15 Clutch Players")
    fig = px.bar(
        clutch.head(15),
        x="clutch_index",
        y="player",
        orientation="h",
        template="plotly_dark",
        color="clutch_index",
        color_continuous_scale="Inferno"
    )
    fig.update_layout(height=600, yaxis=dict(autorange="reversed"))
    st.plotly_chart(fig, use_container_width=True)

with right:
    st.subheader("⚡ Death Over Finishers")
    fig = px.bar(
        death.head(15),
        x="death_score",
        y="player",
        orientation="h",
        template="plotly_dark",
        color="death_score",
        color_continuous_scale="Oranges"
    )
    fig.update_layout(height=600, yaxis=dict(autorange="reversed"))
    st.plotly_chart(fig, use_container_width=True)

st.divider()

st.subheader("🧠 Player Intelligence Explorer")

player_list = sorted(df["batter"].dropna().unique())
selected_player = st.selectbox("Select a player", player_list)

player_df = df[df["batter"] == selected_player]

runs = int(player_df["batsman_runs"].sum())
balls = len(player_df)
boundaries = int((player_df["batsman_runs"] >= 4).sum())
avg_impact = round(player_df["impact_score"].mean(), 2)
avg_pressure = round(player_df["pressure_score"].mean(), 2)

a, b, c, d = st.columns(4)

with a:
    st.markdown(f'<div class="kpi"><h2>{runs}</h2><p>Total Runs</p></div>', unsafe_allow_html=True)

with b:
    st.markdown(f'<div class="kpi"><h2>{balls}</h2><p>Balls Faced</p></div>', unsafe_allow_html=True)

with c:
    st.markdown(f'<div class="kpi"><h2>{boundaries}</h2><p>Boundaries</p></div>', unsafe_allow_html=True)

with d:
    st.markdown(f'<div class="kpi"><h2>{avg_impact}</h2><p>Avg Impact</p></div>', unsafe_allow_html=True)

st.write("")

st.markdown(f"""
<div class="player-card">
    <h2>{selected_player}</h2>
    <p>
    This player has faced <b>{balls}</b> deliveries, scored <b>{runs}</b> runs,
    produced <b>{boundaries}</b> boundary events, and carries an average pressure score of
    <b>{avg_pressure}</b>. MomentumX uses this profile to understand whether the player
    acts as a stabilizer, accelerator, or pressure performer.
    </p>
</div>
""", unsafe_allow_html=True)

st.write("")

phase_data = player_df.groupby("phase")["batsman_runs"].sum().reset_index()

fig = px.pie(
    phase_data,
    names="phase",
    values="batsman_runs",
    template="plotly_dark",
    hole=0.45,
    title=f"{selected_player} Runs by Match Phase"
)

st.plotly_chart(fig, use_container_width=True)