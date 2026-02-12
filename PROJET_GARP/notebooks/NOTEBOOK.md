# Analyse de Performance d'une Stratégie GARP (Growth at a Reasonable Price)

**Master 2 Finance Internationale**

## 📋 Description
Ce projet analyse la performance d'un portefeuille de conviction GARP (10 actions internationales) face aux benchmarks mondiaux sur la période 2021-2026. L'étude décompose l'alpha, évalue l'exposition aux facteurs de risque (Fama-French, Carhart) et teste la persistance de la surperformance.

## 🛠 Technologies
* **Langage :** Python 3.12
* **Données :** Yahoo Finance (`yfinance`), FactSet (indices benchmarks)
* **Bibliothèques :** Pandas, NumPy, Statsmodels (Newey-West errors), Matplotlib/Seaborn.

## 📊 Résultats Clés
* **Performance :** Le portefeuille GARP affiche un ratio de Sharpe de **0.63** contre **0.39** pour le MSCI World.
* **Alpha :** Un alpha annualisé (Carhart 4F) de **8.44%**, bien que la significativité statistique soit limite (p-value ~0.07).
* **Style :** Forte exposition au facteur *Growth* (Beta ~1.12), mais faible exposition au *Value*.
* **Robustesse :** La surperformance se maintient face au FTSE All-World et après prise en compte de coûts de transaction théoriques (20 bps).

## 📂 Structure du Notebook
1.  **Préparation des données :** Univers d'investissement, conversion devises (EUR), rendements mensuels.
2.  **Analyse descriptive :** Métriques de risque (VaR, CVaR, Sortino) et comparaison vs MSCI World.
3.  **Caractérisation stylistique :** Analyse vs MSCI World Growth & Value.
4.  **Décomposition factorielle :** Régressions CAPM, Fama-French 3F et Carhart 4F.
5.  **Persistance :** Rolling Sharpe, Rolling Alpha et analyse par régimes de marché (Bull/Bear).
6.  **Robustesse :** Bootstrap de l'alpha, benchmarks alternatifs et impact des coûts.

## 🚀 Installation et Utilisation
1. Cloner le dépôt.
2. Installer les dépendances : `pip install -r requirements.txt`
3. Lancer le notebook : `jupyter notebook scripts.ipynb`
