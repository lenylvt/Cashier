import streamlit as st

# Titre de l'application
st.title('Calculateur de monnaie')

# Initialisation de la session state pour le total payé
if 'total_paye' not in st.session_state:
    st.session_state['total_paye'] = 0.0

# Entrée pour la somme totale à payer
total_a_payer = st.number_input('Somme totale à payer', min_value=0.0, value=0.0, format="%.2f", help="Entrez la somme totale à payer.")

# Afficher le total payé, la somme totale, et la monnaie à rendre en utilisant st.metric
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total payé", value=f"{st.session_state.total_paye:.2f}€")
with col2:
    st.metric("Somme totale à payer", value=f"{total_a_payer:.2f}€")
with col3:
    monnaie_a_rendre = st.session_state.total_paye - total_a_payer
    st.metric("Monnaie à rendre", value=f"{monnaie_a_rendre if monnaie_a_rendre > 0 else 0:.2f}€")

# Fonction pour ajouter de l'argent au total payé
def ajouter_argent(montant):
    st.session_state.total_paye += montant

# Boutons pour ajouter des montants spécifiques
montants = [0.05, 0.10, 0.20, 0.50, 1, 2, 5, 10, 20, 30, 40, 50]
for index in range(0, len(montants), 3):
    cols = st.columns(3)
    for i, montant in enumerate(montants[index:index+3]):
        with cols[i]:
            if st.button(f"{montant}€"):
                ajouter_argent(montant)
                st.rerun()

# Bouton pour réinitialiser
if st.button('Réinitialiser'):
    st.session_state.total_paye = 0.0
    st.rerun()
