"""
01_data_preparation.py

Objectif :
- Importer les données actions GARP depuis Yahoo Finance
- Convertir toutes les séries en EUR
- Construire un portefeuille GARP équipondéré
- Importer les benchmarks depuis FactSet (Excel)
- Calculer les rendements mensuels
- Aligner toutes les séries sur la période commune
- Exporter les données prêtes pour l'analyse empirique

Master 2 Finance Internationale – Projet GARP
"""

# =========================
# 1. LIBRAIRIES
# =========================

import pandas as pd
import numpy as np
import yfinance as yf
from pathlib import Path

# =========================
# 2. PARAMÈTRES GÉNÉRAUX
# =========================

START_DATE = "2016-02-01"
END_DATE   = "2026-01-31"

DATA_RAW = Path("../data/raw")
DATA_PROCESSED = Path("../data/processed")

DATA_PROCESSED.mkdir(parents=True, exist_ok=True)

# =========================
# 3. UNIVERS GARP
# =========================

GARP_TICKERS = {
    "ADYEN.AS": "EUR",
    "SLYG.DE": "EUR",
    "AMZN": "USD",
    "META": "USD",
    "GOOGL": "USD",
    "CSU.TO": "CAD",
    "MELI": "USD",
    "DNP.WA": "PLN",
    "NU": "USD",
    "KNSL": "USD"
}

# =========================
# 4. TAUX DE CHANGE (vs EUR)
# =========================

FX_TICKERS = {
    "USD": "EURUSD=X",
    "CAD": "EURCAD=X",
    "PLN": "EURPLN=X"
}

# =========================
# 5. IMPORT ACTIONS (YAHOO)
# =========================

prices_local = pd.DataFrame()

for ticker, currency in GARP_TICKERS.items():
    data = yf.download(
        ticker,
        start=START_DATE,
        end=END_DATE,
        interval="1mo",
        auto_adjust=True,
        progress=False
    )["Close"]

    data.name = ticker

    # Conversion en EUR si nécessaire
    if currency != "EUR":
        fx = yf.download(
            FX_TICKERS[currency],
            start=START_DATE,
            end=END_DATE,
            interval="1mo",
            auto_adjust=True,
            progress=False
        )["Close"]

        data = data / fx

    prices_local[ticker] = data

prices_local = prices_local.dropna(how="all")

# =========================
# 6. RENDEMENTS ACTIONS
# =========================

returns_stocks = np.log(prices_local / prices_local.shift(1)).dropna()

# =========================
# 7. PORTEFEUILLE GARP ÉQUIPONDÉRÉ
# =========================

returns_garp = returns_stocks.mean(axis=1)
returns_garp.name = "GARP"

# =========================
# 8. IMPORT BENCHMARKS (FACTSET)
# =========================

def load_factset_index(filename, col_name):
    df = pd.read_excel(DATA_RAW / filename)
    df.iloc[:, 0] = pd.to_datetime(df.iloc[:, 0])
    df.set_index(df.columns[0], inplace=True)
    returns = np.log(df / df.shift(1)).dropna()
    returns.columns = [col_name]
    return returns

benchmarks = pd.concat([
    load_factset_index("msci_world_factset.xlsx", "MSCI_WORLD"),
    load_factset_index("msci_world_growth_factset.xlsx", "MSCI_WORLD_GROWTH"),
    load_factset_index("msci_world_value_factset.xlsx", "MSCI_WORLD_VALUE"),
    load_factset_index("ftse_all_world_factset.xlsx", "FTSE_ALL_WORLD")
], axis=1)

# =========================
# 9. ALIGNEMENT FINAL
# =========================

returns_all = pd.concat(
    [returns_garp, benchmarks],
    axis=1
).dropna()

# =========================
# 10. EXPORT
# =========================

returns_all.to_csv(DATA_PROCESSED / "monthly_returns_garp_benchmarks.csv")

print("✔ Data preparation completed successfully")
print(f"✔ Observations: {returns_all.shape[0]}")
print(f"✔ Period: {returns_all.index.min().date()} → {returns_all.index.max().date()}")

