import numpy as np

class EcoEnv:
    def __init__(self, data, prefs):
        self.data = data
        self.prefs = prefs
        self.state = self.build_state()

        self.action_labels = [
            "Réduire chauffage",
            "Prendre le vélo",
            "Réduire viande",
            "Réduire eau",
            "Réduire déchets",
            "Installer panneaux solaires"
        ]

        self.action_explanations = [
            "Diminuer la température permet d'économiser immédiatement de l'énergie.",
            "Le vélo est un mode propre et bénéfique pour la santé.",
            "Réduire la viande réduit fortement l'empreinte carbone.",
            "Réduire la consommation d'eau allège les réseaux et le traitement.",
            "Moins de déchets, plus de recyclage et moins d'incinération.",
            "Les panneaux solaires permettent une production propre et locale."
        ]

    def build_state(self):
        base = np.array([
            self.data["energy"]["electricity_kWh"] / 1000,
            self.data["energy"]["gas_kWh"] / 1000,
            self.data["transport"]["co2_emission_kg"] / 100,
            self.data["food"]["avg_calories"] / 2500,
            self.data["food"]["meat_ratio"] / 100,
            self.data["population"] / 1_000_000,
            self.data["energy"]["renewable_ratio"]
        ])
        user = np.array([
            1.0 if self.prefs["vegan"] else 0.0,
            1.0 if self.prefs["teletravail"] else 0.0,
            {"Voiture": 1, "Train": 0.6, "Bus": 0.7, "Vélo": 0.1, "Marche": 0.0}[self.prefs["transport"]],
            self.prefs["chauffage"] / 24.0,
            self.prefs["eau"] / 300,
            self.prefs["dechets"] / 30,
            {"Oui": 0, "Partiel": 0.5, "Non": 1}[self.prefs["tri"]],
            {"Île-de-France": 0.8, "Occitanie": 1.3, "PACA": 1.4, "Bretagne": 1.0, "Hauts-de-France": 0.75}[self.prefs["region"]]
        ])
        return np.concatenate([base, user])

    def step(self, action):
        reward = np.random.uniform(0.2, 1.5)
        self.state += np.random.normal(0, 0.01, size=self.state.shape)
        return self.state, reward
