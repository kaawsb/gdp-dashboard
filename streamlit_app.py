# ==============================================================
# 1D DC Forward Modelling (SimPEG) — Schlumberger + Wenner
# Version "optimisée & pédagogique" avec interface Streamlit
#
# Ce fichier réalise un sondage électrique vertical (1D VES)
# en utilisant la méthode du courant continu (DC resistivity).
# Il simule deux dispositifs classiques :
#   - Schlumberger
#   - Wenner
# Et trace les courbes de résistivité apparente rho_a(AB/2)
# pour un modèle de couches donné (rho + épaisseurs).
#
# Tout est expliqué en détail dans les commentaires (#)
# ==============================================================


# ==============================================================
# 0) IMPORTS DES LIBRAIRIES
# ==============================================================

import numpy as np                 # Calcul scientifique (tableaux + log + géométrique)
import pandas as pd               # Tableaux de données (pour afficher et exporter en CSV)
import matplotlib.pyplot as plt   # Graphiques (courbes, modèle 1D)
import streamlit as st            # Interface web Streamlit

# Import du module DC Resistivity de SimPEG (électrostatique)
from simpeg.electromagnetics.static import resistivity as dc

# maps.IdentityMap permet de dire : "mon modèle = ma résistivité directement"
from simpeg import maps

# Outils pour axes logarithmiques propres
from matplotlib.ticker import LogLocator, LogFormatter, NullFormatter


# ==============================================================
# 1) STYLE CSS — personnalisation visuelle de Streamlit
# ==============================================================

# On injecte du CSS pour rendre l'application plus agréable à l'œil.
# Ce bloc modifie :
#   - la couleur de fond
#   - l'apparence de la sidebar
#   - la présentation des tableaux Streamlit
st.markdown(
    """
    <style>
    .stApp {
        /* Couleur d’arrière-plan générale */
        background-color: #f7f8fb;
    }

    h1, h2, h3 {
        /* Couleur des titres */
        color: #1f4e79;
    }

    /* Style de la barre latérale */
    section[data-testid="stSidebar"] {
        background-color: #f0f2f6;
        border-right: 1px solid #d5d8dd;
    }

    /* Style pour les DataFrames Streamlit */
    .stDataFrame {
        background-color: white;
        border-radius

