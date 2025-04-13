import streamlit as st
import json
import os
from dqn_agent import DQNAgent
from environment import EcoEnv
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="EcoBrain v4", layout="wide")

# Charger les données régionales
data_path = os.path.join("data", "sample_data.json")
if not os.path.exists(data_path):
    st.error("Fichier de données introuvable : data/sample_data.json")
    st.stop()

with open(data_path) as f:
    data = json.load(f)

# Préférences utilisateur (module IA intégré)
st.sidebar.header("🔧 Vos préférences")
prefs = {
    "vegan": st.sidebar.checkbox("Régime végétarien/végétalien"),
    "teletravail": st.sidebar.checkbox("Télétravail aujourd'hui"),
    "transport": st.sidebar.selectbox("Transport principal", ["Voiture", "Train", "Bus", "Vélo", "Marche"]),
    "chauffage": st.sidebar.slider("Température intérieure (°C)", 16, 24, 20),
    "eau": st.sidebar.slider("Conso. d'eau (L/jour)", 50, 300, 150),
    "dechets": st.sidebar.slider("Déchets (kg/semaine)", 0, 30, 12),
    "tri": st.sidebar.radio("Tri sélectif ?", ["Oui", "Partiel", "Non"]),
    "region": st.sidebar.selectbox("Région", ["Île-de-France", "Occitanie", "PACA", "Bretagne", "Hauts-de-France"])
}

# Initialiser environnement + agent
env = EcoEnv(data, prefs)
agent = DQNAgent(state_size=len(env.state), action_size=6)

if "state" not in st.session_state:
    st.session_state.state = env.state
    st.session_state.rewards = []
    st.session_state.actions = []

state = st.session_state.state
action = agent.act(state)

# Affichage conseil
st.title("🌍 EcoBrain v4 – IA augmentée")
st.subheader("📌 Conseil IA personnalisé")
st.markdown(f"**{env.action_labels[action]}**")
st.caption(env.action_explanations[action])

if st.button("✅ Appliquer ce conseil"):
    next_state, reward = env.step(action)
    agent.remember(state, action, reward, next_state)
    agent.train()
    st.session_state.state = next_state
    st.session_state.rewards.append(reward)
    st.session_state.actions.append(env.action_labels[action])

# Résultats
st.metric("Score environnemental", round(sum(st.session_state.rewards), 2))
st.metric("CO2 actuel (kg)", round(state[2], 2))
st.metric("Électricité (kWh)", round(state[0], 2))

if st.session_state.rewards:
    st.line_chart(st.session_state.rewards, height=200)

with st.expander("Voir l’historique des actions appliquées"):
    for i, a in enumerate(st.session_state.actions, 1):
        st.write(f"{i}. {a}")
