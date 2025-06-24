# 📊 Pilotage de la Production – Organisme Public (données simulées)

## 🎯 Objectif du projet  
Développer un tableau de bord interactif pour suivre la performance d'équipes traitant des dossiers administratifs.  
Ce projet vise à améliorer la visibilité sur les délais de traitement, la charge de travail et les points de blocage à l’aide de **KPI dynamiques**, de **filtres intuitifs** et de **recommandations automatiques**.

🔗 **Lien vers l'application Streamlit** :  
👉 [Accéder à l'application](https://pilotage-appuction-organisme-public-gnjpui2nu66lmc4ked96zl.streamlit.app/)

---

## 📁 Données simulées

| Colonne              | Description                                                        |
|----------------------|--------------------------------------------------------------------|
| Date                 | Date de traitement du dossier                                      |
| Service              | Unité ou entité traitante                                          |
| Type_dossier         | Catégorie du dossier (Ex : Retraite, Invalidité, etc.)             |
| Statut               | Clôturé ou en cours                                                |
| Délai_traitement     | Nombre de jours avant clôture                                      |
| Nb_documents         | Nombre de pièces jointes associées                                 |
| Retours_dossier      | Nombre de fois où le dossier a été retourné                        |
| Agent                | ID anonyme du gestionnaire                                         |
| Dossiers_traites     | Nombre total de dossiers clôturés                                  |
| Taux_retour          | Ratio entre retours et dossiers traités                            |
| Charge_workload      | Charge estimée pondérée selon type et délai                        |

---

## ⚙️ Fonctionnalités principales

- 🎛️ Filtres dynamiques (par service, type de dossier, période)
- 📦 Indicateurs clés de performance :
  - Nombre de dossiers traités
  - Délai moyen de traitement
  - Taux de retour des dossiers
- 📈 Visualisations interactives :
  - Évolution mensuelle des traitements
  - Analyse comparative entre services
- 🧠 Recommandations automatiques selon seuils critiques
- 📥 Export des données filtrées au format CSV

---

## 🛠️ Stack technique

- Python  
- Pandas  
- Plotly Express  
- Streamlit  

---

## 🧠 Méthodologie

| Étape                             | Description                                                                 |
|----------------------------------|-----------------------------------------------------------------------------|
| 1. Simulation des données        | Génération d’un jeu de données réaliste avec plusieurs variables métier     |
| 2. Préparation & nettoyage       | Traitement des formats, gestion des valeurs manquantes, conversions         |
| 3. Développement applicatif      | Conception de l’interface avec Streamlit                                    |
| 4. Calcul des indicateurs clés   | Dossiers traités, délais, retours, charges                                  |
| 5. Visualisation & UX            | Graphiques, filtres, métriques et export                                    |
| 6. Mise en ligne                 | Déploiement via Streamlit Cloud, accessible publiquement                    |

---

## 📌 Résultats et insights

- Mise en lumière des écarts de performance entre services
- Détection de délais de traitement supérieurs à la norme (>20 jours)
- Taux de retour élevé identifiant les points de friction
- Simulation d’aide à la décision pour optimiser la charge et réduire les délais

---

## 💬 Recommandations

- 📍 Repenser la distribution des charges si les écarts entre services persistent  
- 🔍 Identifier les causes des taux de retour élevés (qualité des documents, erreurs de saisie…)  
- 👥 Allouer des renforts temporaires en cas de pics de charge  

---

## 👤 À propos

Je suis **S. Kodon**, Data Analyst passionné par le pilotage opérationnel, les outils de visualisation et la prise de décision appuyée par la donnée.  
Ce projet s'inscrit dans une série de démonstrateurs interactifs que je développe pour illustrer ma capacité à transformer des données en outils d’action concrets.

👉 [Autres projets disponibles ici](https://github.com/Samadkod)

---
