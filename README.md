---

# **HermesLedger**

🌿 **HermesLedger — Chaîne PoA pour Logs**

**HermesLedger** est une blockchain Proof-of-Authority minimale conçue pour stocker immuablement les journaux (logs) ou traces d’audit de serveurs.

---

## 🎯 **Qu’est-ce que c’est ?**

**HermesLedger** est une démonstration d’une blockchain interne en Proof-of-Authority (PoA), permettant d’enregistrer des logs de serveurs dans un registre distribué, infalsifiable et vérifiable dans le temps.

---

## ⚙️ **Ce que contient le projet**

* `src/` : Code Python de la mini blockchain PoA et simulation de nœuds
* `docker/` : Dockerfile + docker-compose pour 3 nœuds de démonstration
* `README.md` : Ce fichier
* `LICENSE` : Licence MIT

---

## 🚀 **Démarrage rapide (Python local)**

1. Installer **Python 3.11**
2. Exécuter :

   ```bash
   python src/run_demo.py
   ```
3. Observer les logs et la chaîne affichés en console

---

## 🐳 **Démarrage rapide (Docker Compose)**

1. Aller dans `docker`
2. Lancer :

   ```bash
   docker-compose up --build
   ```
3. Chaque conteneur exécutera `run_demo.py` (comportement de démonstration)

---

## 🧭 **Pourquoi le PoA pour les logs ?**

* Faible consommation énergétique
* Finalité rapide & haut débit
* Autorités = serveurs connus (confiance maîtrisée en interne)

---

## 📝 **Licence**

Ce projet est publié sous la **Licence MIT**.

---