# PROJET_GARP  
**Analyse de la performance d’une stratégie de conviction GARP (Growth at a Reasonable Price)**  
*Décomposition factorielle de l’alpha et évaluation de la persistance du couple rendement–risque*

---

## Contexte académique

Ce projet s’inscrit dans le cadre du **Master 2 Finance Internationale (IAE Metz – Université de Lorraine)**, au sein d’un enseignement dédié à la **finance empirique et à l’analyse quantitative de stratégies d’investissement**.

L’objectif est de mettre en œuvre, à l’aide de Python, une analyse rigoureuse de la performance d’une stratégie actions de type **GARP (Growth at a Reasonable Price)**, en mobilisant les outils standards de l’évaluation de la gestion active.

---

## Problématique

> **La stratégie GARP du portefeuille génère-t-elle une surperformance durable et significative en rendement ajusté du risque par rapport aux benchmarks actions mondiaux, et cette performance est-elle expliquée par des expositions factorielles connues ou par un alpha résiduel propre ?**

Cette problématique s’inscrit au cœur du débat entre **gestion active et gestion passive**, ainsi que dans la littérature sur les **facteurs de performance** et la persistance de l’alpha.

---

## Hypothèses de recherche

- **H1** — Le portefeuille GARP surperforme le benchmark mondial en termes de rendement ajusté du risque. 
- **H2** — L’alpha du portefeuille GARP est partiellement expliqué par des expositions factorielles.  
- **H3** — Une fraction résiduelle de l’alpha demeure statistiquement significative.  
- **H4** — Le couple rendement–risque du portefeuille GARP est persistant dans le temps.

---

## Benchmarks utilisés

Les performances de la stratégie GARP sont évaluées relativement aux indices suivants :

- **MSCI World**  
  Le MSCI World est utilisé comme benchmark principal car il représente le portefeuille actions mondial passif de référence pour un investisseur international. Il permet d’évaluer la surperformance globale du portefeuille GARP et de mesurer la valeur ajoutée de la gestion active en termes de rendement ajusté du risque.

- **MSCI World Growth**  
  Le MSCI World Growth est retenu afin de déterminer si la performance du portefeuille GARP s’explique principalement par une exposition croissance classique ou par une approche GARP distincte. Il permet de comparer les profils de performance et de risque à un style growth pur.

- **MSCI World Value**  
  Le MSCI World Value est utilisé pour situer le portefeuille GARP par rapport au style value et analyser son comportement relatif au cours des différents cycles de marché. Il permet de positionner la stratégie GARP à l’intersection des styles growth et value.

- **FTSE All-World**  
  Le FTSE All-World est intégré comme benchmark alternatif afin de tester la robustesse des résultats face à une méthodologie de construction d’indice différente de celle de MSCI. Il permet de vérifier que les conclusions ne dépendent pas d’un fournisseur d’indice spécifique.

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
```text
PROJET_GARP/
│
├── data/
│   ├── raw/                # Données brutes
│   ├── processed/          # Données nettoyées et alignées
│
├── scripts/
│   ├── scripts.ipynb
│   
│
├── results/
│   ├── tables/
│   ├── figures/
│
├── notebooks/              
│
├── README.md               # Présentation académique du projet
└── requirements.txt        # Librairies Python
```

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




