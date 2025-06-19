import streamlit as st
import pandas as pd
import plotly.express as px

# Chargement des données
df = pd.read_csv("donnees_simulees_cnav.csv", parse_dates=["Date"])

st.set_page_config(page_title="Pilotage Production - CNAV", layout="wide")

st.title("📊 Suivi de la performance - Production CNAV")
st.markdown("Analyse des dossiers, délais et performances mensuelles")

# Filtres
col1, col2 = st.columns(2)
with col1:
    types = st.multiselect("Type de dossier", df["Type_dossier"].unique(), default=df["Type_dossier"].unique())
with col2:
    agences = st.multiselect("Agence", df["Agence"].unique(), default=df["Agence"].unique())

df_filtered = df[df["Type_dossier"].isin(types) & df["Agence"].isin(agences)]

# KPI principaux
col3, col4, col5 = st.columns(3)
col3.metric("📦 Dossiers traités", int(df_filtered["Dossiers_traites"].sum()))
col4.metric("⏱️ Délai moyen (jours)", round(df_filtered["Délai_traitement"].mean(), 1))
col5.metric("⚠️ Taux de retour", f"{df_filtered['Taux_retour'].mean():.1%}")

# Graphique des dossiers traités par mois
fig1 = px.bar(df_filtered.groupby(df_filtered["Date"].dt.to_period("M"))["Dossiers_traites"].sum().reset_index(),
              x="Date", y="Dossiers_traites", title="📈 Évolution mensuelle des dossiers traités")
st.plotly_chart(fig1, use_container_width=True)

# Graphique du délai moyen par agence
fig2 = px.box(df_filtered, x="Agence", y="Délai_traitement", color="Agence",
              title="⏳ Délai moyen par agence")
st.plotly_chart(fig2, use_container_width=True)

# Téléchargement des données filtrées
st.download_button("📥 Télécharger les données filtrées", data=df_filtered.to_csv(index=False),
                   file_name="donnees_cnav_filtrees.csv", mime="text/csv")

# Recommandations simples
st.subheader("💡 Recommandations automatiques")
if df_filtered["Délai_traitement"].mean() > 20:
    st.warning("⏱️ Le délai moyen dépasse 20 jours. Envisagez un renfort temporaire ou une révision des procédures.")
if df_filtered["Taux_retour"].mean() > 0.1:
    st.error("❌ Le taux de retour dépasse 10%. Un audit des motifs est recommandé.")
if df_filtered.groupby("Agence")["Dossiers_traites"].sum().std() > 300:
    st.info("📍 Écart important entre agences. Une redistribution des charges peut être envisagée.")

