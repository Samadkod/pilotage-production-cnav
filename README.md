# 📊 Pilotage de la Production – CNAV

🎯 **Objectif du projet**  
Développer un tableau de bord interactif pour suivre la performance des équipes de traitement de dossiers au sein d’un organisme public (inspiré de la CNAV), via des indicateurs clairs et des visualisations dynamiques.

🔗 **Lien vers l'application** :  
👉 [Accéder à l'application Streamlit](https://pilotage-appuction-cnav-aenhnxkzdjkwnqfcpcleid.streamlit.app/)

---

## 📁 Données simulées

| Colonne              | Description                                                        |
|----------------------|--------------------------------------------------------------------|
| Date                 | Date de traitement du dossier                                      |
| Agence               | Nom de l'agence CNAV concernée                                     |
| Type_dossier         | Type de dossier : Retraite, Invalidité, Survie, etc.               |
| Statut               | Clôturé ou en cours                                                |
| Délai_traitement     | Nombre de jours avant clôture                                      |
| Nb_documents         | Nombre de documents associés au dossier                            |
| Retours_dossier      | Nombre de fois où le dossier a été retourné                        |
| Agent                | ID de l’agent ayant traité le dossier                              |
| Dossiers_traites     | Nombre de dossiers clôturés par ligne                              |
| Taux_retour          | Ratio entre retours et traitements                                |
| Charge_workload      | Charge estimée (pondération selon type et délai)                   |
---

## ⚙️ Fonctionnalités principales

- 🎛️ Filtres dynamiques (agence & type de dossier)
- 📦 Indicateurs clés de performance :
  - Nombre de dossiers traités
  - Délai moyen de traitement
  - Taux de retour
- 📈 Visualisations :
  - Évolution mensuelle des dossiers traités
  - Analyse du délai moyen par agence
- 🧠 Recommandations automatiques selon seuils critiques
- 📥 Export des données filtrées en un clic

---

## 🛠️ Stack utilisée

- Python
- Pandas
- Plotly Express
- Streamlit

---

## 📌 Résultats et insights

- Mise en lumière des écarts de performance entre agences
- Détection de délais de traitement supérieurs à la norme (>20 jours)
- Taux de retour élevé identifiant les points de friction
- Simulation d’aide à la décision pour optimiser la charge et réduire les délais

---

## 💬 Recommandations métiers

- 📍 Revoir la répartition des charges entre agences si l’écart-type dépasse un seuil critique
- 🔍 Auditer les dossiers avec taux de retour élevé pour identifier les causes (documents manquants, mauvaise saisie…)
- 👥 Proposer des renforts temporaires dans les agences avec forte pression

---

## 🧑‍💼 À propos

👋 Je suis **S. Kodon**, Data Analyst passionné par le pilotage de la performance et les solutions concrètes basées sur la donnée. Je suis actuellement à la recherche d’un **CDD, CDI ou contrat pro** dans le domaine de la data, du reporting ou des études statistiques.

📧 Contactez-moi directement sur [LinkedIn](https://www.linkedin.com/in/ton-profil) ou en téléchargeant mon [CV ici](https://tonliencv.fr).

---

✅ Projet entièrement disponible sur GitHub :
[https://github.com/Samadkod/pilotage-production-cnav](https://github.com/Samadkod/pilotage-production-cnav)
