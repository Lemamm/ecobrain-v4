# 🌍 EcoBrain v4 – IA augmentée pour la transition écologique

**EcoBrain v4** est un prototype d’intelligence artificielle régulatrice capable de proposer des actions durables personnalisées, basées sur :

- Vos habitudes de vie (transport, chauffage, alimentation…)
- Les données moyennes de votre région
- Une intelligence artificielle (DQN) pour apprendre, prédire et s’adapter

---

## 🧠 Fonctionnalités

- ✅ Conseils IA contextuels en temps réel
- 🌱 Modules intégrés : mobilité, eau, déchets, alimentation, énergie, solaire
- 📊 Visualisation des impacts environnementaux simulés
- 🔒 Respect de la vie privée (aucune donnée personnelle traitée)
- 🧩 Architecture modulaire (environnement simulé + IA DQN)

---

## 📁 Structure du projet

ecobrain_v4_ai/ ├── app.py ← Interface principale Streamlit ├── environment.py ← Environnement simulant l’impact des actions ├── dqn_agent.py ← Agent DQN (Deep Q-Learning) ├── requirements.txt ← Dépendances Python └── data/ └── sample_data.json ← Données simulées régionales


---

## 📌 Objectif

Créer un "cerveau planétaire" éthique, transparent et non discriminant capable de guider les populations vers une réduction collective de leur impact écologique.

    🤖 L’IA vous guide, mais vous restez libre. Aucune contrainte, que des recommandations.

🧑‍💻 Auteurs

Projet imaginé par Lemamm
Contributions bienvenues : Forkez, testez, proposez vos modules !

## 🚀 Lancer en local

```bash
git clone https://github.com/Lemamm/ecobrain_v4_ai.git
cd ecobrain_v4_ai
pip install -r requirements.txt
streamlit run app.py



