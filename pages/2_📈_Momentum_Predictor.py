import streamlit as st
import pandas as pd
import joblib
import numpy as np

st.set_page_config(page_title="Momentum Predictor", layout="wide")

st.markdown("""
<style>
.stApp {
    background: radial-gradient(circle at top left, #111827, #020617 55%, #000000);
    color: white;
}

.title {
    font-size: 42px;
    font-weight: 900;
    background: linear-gradient(90deg, #facc15, #fb923c, #ef4444);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.result-card {
    padding: 28px;
    border-radius: 24px;
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.18);
    box-shadow: 0 15px 45px rgba(0,0,0,0.4);
}

.result-card h2 {
    color: #facc15;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">📈 Momentum Shift Predictor</div>', unsafe_allow_html=True)
st.caption("Predict whether the current IPL match situation can trigger a momentum shift.")

model = joblib.load("momentumx_grand_model.pkl")
features = joblib.load("advanced_features.pkl")

st.write("")
st.subheader("Enter Match Situation")

col1, col2, col3 = st.columns(3)

with col1:
    over = st.slider("Over Number", 0, 19, 15)
    batsman_runs = st.number_input("Runs on Current Ball", 0, 6, 1)
    extras = st.number_input("Extras on Current Ball", 0, 6, 0)

with col2:
    total_runs = st.number_input("Total Runs on Current Ball", 0, 10, 1)
    current_rr = st.number_input("Current Run Rate", 0.0, 25.0, 8.5)
    boundary_count = st.number_input("Boundary Count So Far", 0, 50, 12)

with col3:
    wickets_lost = st.number_input("Wickets Lost", 0, 10, 4)
    recent_runs = st.number_input("Recent Runs Last 6 Balls", 0, 36, 8)

pressure_score = 0

if over >= 15:
    pressure_score += 3

if total_runs == 0:
    pressure_score += 1

if wickets_lost >= 6:
    pressure_score += 2

impact_score = (
    batsman_runs * 1.5
    - pressure_score * 0.5
)

momentum = (
    total_runs
    - (wickets_lost * 0.2)
)

volatility_score = (
    impact_score * 0.5
    + pressure_score * 0.3
    + momentum * 0.2
)

input_data = pd.DataFrame({
    "over": [over],
    "batsman_runs": [batsman_runs],
    "extras": [extras],
    "total_runs": [total_runs],
    "current_rr": [current_rr],
    "boundary_count": [boundary_count],
    "wickets_lost": [wickets_lost],
    "recent_runs": [recent_runs]
})

for col in features:
    if col not in input_data.columns:
        input_data[col] = 0

input_data = input_data[features]

if st.button("Analyze Momentum", use_container_width=True):
    prediction = model.predict(input_data)[0]

    if hasattr(model, "predict_proba"):
        probability = model.predict_proba(input_data)[0][1] * 100
    else:
        probability = 0

    if pressure_score >= 5:
        pressure_level = "High Pressure"
    elif pressure_score >= 3:
        pressure_level = "Medium Pressure"
    else:
        pressure_level = "Low Pressure"

    if wickets_lost >= 7:
        collapse_risk = "High Collapse Risk"
    elif wickets_lost >= 4:
        collapse_risk = "Moderate Collapse Risk"
    else:
        collapse_risk = "Low Collapse Risk"

    if momentum > 3:
        dominance = "Batting Side Dominating"
    elif momentum > 1:
        dominance = "Balanced Situation"
    else:
        dominance = "Batting Side Under Pressure"

    if prediction == 1:
        result = "Momentum Shift Likely"
    else:
        result = "No Major Momentum Shift"

    st.write("")
    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown(f"""
        <div class="result-card">
            <h2>{round(probability, 2)}%</h2>
            <p>Momentum Shift Probability</p>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown(f"""
        <div class="result-card">
            <h2>{pressure_level}</h2>
            <p>Pressure Level</p>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown(f"""
        <div class="result-card">
            <h2>{collapse_risk}</h2>
            <p>Collapse Risk</p>
        </div>
        """, unsafe_allow_html=True)

    with c4:
        st.markdown(f"""
        <div class="result-card">
            <h2>{dominance}</h2>
            <p>Dominance Status</p>
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.markdown(f"""
    <div class="result-card">
        <h2>AI Verdict: {result}</h2>
        <p>
        The system analyzed over number, scoring pattern, wickets lost, recent runs,
        boundary count and run-rate pressure to estimate match momentum.
        </p>
    </div>
    """, unsafe_allow_html=True)