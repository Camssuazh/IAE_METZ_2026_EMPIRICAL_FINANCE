# PROJET_GARP  
**Analyse de la performance d’une stratégie de conviction GARP (Growth at a Reasonable Price)**  
*Décomposition factorielle de l’alpha et évaluation de la persistance du couple rendement–risque*

---

## Contexte académique

Ce projet s’inscrit dans le cadre du **Master 2 Finance Internationale (IAE Metz – Université de Lorraine)**, au sein d’un enseignement dédié à la **finance empirique et à l’analyse quantitative de stratégies d’investissement**.

L’objectif est de mettre en œuvre, à l’aide de Python, une analyse rigoureuse de la performance d’une stratégie actions de type **GARP (Growth at a Reasonable Price)**, en mobilisant les outils standards de l’évaluation de la gestion active.

---

## Problématique

> **La stratégie GARP génère-t-elle une surperformance durable et significative en rendement ajusté du risque par rapport aux benchmarks actions mondiaux, et cette performance est-elle expliquée par des expositions factorielles connues ou par un alpha résiduel propre ?**

Cette problématique s’inscrit au cœur du débat entre **gestion active et gestion passive**, ainsi que dans la littérature sur les **facteurs de performance** et la persistance de l’alpha.

---

## Hypothèses de recherche

- **H1** — La stratégie GARP surperforme le benchmark mondial en termes de rendement ajusté du risque.  
- **H2** — L’alpha de la stratégie GARP est partiellement expliqué par des expositions factorielles systématiques.  
- **H3** — Une fraction résiduelle de l’alpha demeure statistiquement significative après contrôle des facteurs.  
- **H4** — Le couple rendement–risque de la stratégie GARP est persistant dans le temps.

---

## Benchmarks utilisés

Les performances de la stratégie GARP sont évaluées relativement aux indices suivants :

- **MSCI World**  
  Benchmark principal représentant le portefeuille actions mondial passif de référence pour un investisseur international.

- **MSCI World Growth**  
  Utilisé afin d’identifier si la performance du portefeuille GARP reflète une exposition à un style growth classique.

- **MSCI World Value**  
  Permet de positionner la stratégie GARP par rapport au style value et d’analyser son comportement au cours des cycles de marché.

- **FTSE All-World**  
  Benchmark alternatif intégré afin de tester la robustesse des résultats face à une méthodologie de construction d’indice différente.

---

## Méthodologie empirique

L’analyse est structurée en plusieurs étapes successives :

1. **Préparation et nettoyage des données**  
   Importation des données de prix, calcul des rendements, alignement temporel et traitement des valeurs manquantes.

2. **Analyse descriptive et performance globale**  
   Évaluation de la performance absolue et relative du portefeuille GARP (rendement, volatilité, Sharpe ratio, drawdown).

3. **Caractérisation stylistique du portefeuille**  
   Comparaison du profil de performance et de risque avec les indices Growth et Value.

4. **Décomposition factorielle de la performance**  
   Estimation de modèles CAPM et Fama-French afin d’identifier les expositions factorielles et l’alpha résiduel.

5. **Analyse de la persistance du couple rendement–risque**  
   Étude de la stabilité temporelle des performances via des analyses rolling et par sous-périodes.

6. **Analyse de robustesse**  
   Vérification de la solidité des résultats face à des benchmarks alternatifs et à différents découpages temporels.

---

## Structure du projet

PROJET_GARP
- data
 -- raw
 -- processed
- scripts
 -- 01_data_preparation.py
 -- 02_descriptive_performance.py
 -- 03_style_analysis.py
 -- 04_factor_decomposition.py
 -- 05_persistence_analysis.py
 -- 06_robustness_checks.py
- results
 -- tables
 -- figures
- notebooks
- README.md
- requirements.txt

---

## Environnement technique

Le projet est développé en **Python** et repose notamment sur les bibliothèques suivantes :

- `pandas`
- `numpy`
- `matplotlib`
- `scipy`
- `statsmodels`
- `yfinance`

L’ensemble des dépendances est listé dans le fichier `requirements.txt`.

---

##  Remarque

Ce projet a une vocation **académique et pédagogique**. Les résultats obtenus ne constituent pas une recommandation d’investissement.

---




