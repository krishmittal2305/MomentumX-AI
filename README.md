# 🏏 MomentumX AI  
### AI-Powered IPL Momentum, Clutch & Match Intelligence Platform

MomentumX AI is a professional sports analytics platform built to analyze IPL ball-by-ball data and extract deep cricket intelligence beyond traditional scorecards.

Instead of only showing runs, wickets, and averages, MomentumX AI focuses on the real questions:

- Who actually changes match momentum?
- Which players perform under pressure?
- Which teams collapse in tough phases?
- Who are the best death-over finishers?
- Which players are best for fantasy picks?
- What does AI predict about match situations?

---

## 🚀 Project Overview

MomentumX AI combines machine learning, cricket analytics, and interactive dashboards to create a complete IPL intelligence system.

The platform studies historical IPL delivery-level data and generates insights such as:

- Momentum shift prediction  
- Clutch player ranking  
- Pressure analysis  
- Collapse risk detection  
- Team dominance ranking  
- AI best XI generation  
- Fantasy team recommendation  
- IPL 2026 trophy prediction  
- AI cricket assistant  
- Player DNA profiles  
- AI commentary generation  

This project is designed as a complete AI-powered cricket analytics ecosystem.

---

## 🎯 Problem Statement

Most cricket analysis focuses on basic statistics like total runs, wickets, strike rate, or economy rate.

But cricket matches are often decided by hidden factors such as:

- Pressure moments  
- Death-over performance  
- Momentum swings  
- Wicket clusters  
- Collapse risk  
- Match phase impact  
- Player clutch behavior  

MomentumX AI solves this gap by analyzing the context behind every delivery and converting raw ball-by-ball data into meaningful match intelligence.

---

## ✨ Key Features

### 📈 Momentum Shift Predictor
Predicts whether a match situation is likely to create a momentum shift using advanced match context features.

### 🔥 ClutchSense Analytics
Ranks players based on pressure handling, impact score, momentum contribution, and death-over performance.

### ⚠️ Pressure Engine
Analyzes pressure phases, wicket clusters, dot-ball pressure, and team collapse risk.

### 🧠 AI Insights Engine
Generates cricket-style analytical insights from player, team, and match behavior.

### 🎮 Match Simulator
Allows users to simulate IPL match situations and receive AI-based momentum and pressure verdicts.

### ⚔️ Player vs Player Comparison
Compares two IPL players using runs, impact score, pressure score, boundaries, and momentum contribution.

### 🏆 AI Best XI Generator
Generates the strongest AI-selected playing XI based on player performance intelligence.

### 🎯 Fantasy Team Engine
Recommends fantasy team picks, captain, vice-captain, safe picks, and differential picks.

### 🏆 IPL 2026 Prediction Center
Predicts tournament power rankings, playoff contenders, and potential title favorites.

### 🤖 AI Cricket Assistant
Allows users to ask IPL-related questions and receive data-driven responses.

### 🧬 Player DNA Profiles
Creates AI-based player personality profiles such as Momentum Accelerator, Pressure Warrior, Clutch Performer, and Match Stabilizer.

### 🎙️ AI Commentary Generator
Generates cricket-style AI commentary for match situations.

---

## 🧠 Machine Learning Model

The ML model predicts momentum-shifting events using match-context features such as:

- Over number  
- Runs on ball  
- Extras  
- Total runs  
- Current run rate  
- Boundary count  
- Wickets lost  
- Recent runs  

The model was trained using a Random Forest Classifier and achieved strong predictive performance after removing data leakage.

---

## 🏗️ Tech Stack

| Area | Technology |
|---|---|
| Programming Language | Python |
| Frontend | Streamlit |
| Data Processing | Pandas, NumPy |
| Machine Learning | Scikit-learn |
| Model Saving | Joblib |
| Visualization | Plotly, Matplotlib, Seaborn |
| Dataset | IPL ball-by-ball JSON data |
| Deployment | Streamlit Community Cloud |

---

## 📂 Project Structure

```text
MomentumX-AI/
│
├── app.py
├── requirements.txt
├── README.md
│
├── momentumx_grand_model.pkl
├── advanced_features.pkl
│
├── final_momentumx_dataset.csv
├── clutch_players.csv
├── death_players.csv
├── team_momentum.csv
├── collapse_risk.csv
├── player_intelligence.csv
│
├── pages/
│   ├── 1_🏏_Dashboard.py
│   ├── 2_📈_Momentum_Predictor.py
│   ├── 3_🔥_Clutch_Analytics.py
│   ├── 4_⚠️_Pressure_Engine.py
│   ├── 5_🧠_AI_Insights.py
│   ├── 6_🎮_Match_Simulator.py
│   ├── 7_⚔️_Player_Comparison.py
│   ├── 8_🏆_Best_XI_Generator.py
│   ├── 9_🎯_Fantasy_Team_Engine.py
│   ├── 10_🏆_IPL_2026_Prediction_Center.py
│   ├── 11_🤖_AI_Cricket_Assistant.py
│   ├── 12_🧬_Player_DNA.py
│   └── 13_🎙️_AI_Commentary.py
│
└── assets/
    ├── ipl_banner.jpg
    ├── player.jpg
    └── other images