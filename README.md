# 📈 Stock Screener & Fundamental Valuation Module

A modular Python and Streamlit application for fetching, processing, and analyzing fundamental stock metrics using `yfinance` and `pandas`.

## 🌟 Key Features

- **Defensive Data Fetching:** Robust handling of ticker errors and missing API fields with multiple fallback mechanisms (`currentPrice` vs `regularMarketPrice`).
- **Multi-Factor Valuation Engine:** Sector-adjusted valuation ratings based on combined analysis of **PEG Ratio**, **P/E Ratio**, and **EV/EBITDA**.
- **Consolidated Pandas DataFrames:** Multi-ticker batch processing with standardized data types.
- **Interactive Streamlit UI:** Standalone user interface for live filtering and fundamental inspection.

## 📁 Project Structure
```text
stock-screener/
├── src/
│   ├── data_fetcher.py      # Raw API interface & defensive checks
│   ├── data_processor.py    # Multi-factor valuation scoring & DataFrame normalization
│   └── app.py               # Standalone Streamlit application
├── venv/                    # Virtual environment
├── .gitignore
└── README.md
```
🚀 Quick Start
Activate Virtual Environment:

Bash
source venv/Scripts/activate
Install Dependencies:

Bash
pip install yfinance pandas streamlit
Run Standalone Streamlit App:

Bash
streamlit run src/app.py
📊 Valuation Signal Methodology
The valuation logic applies sector-adjusted thresholds to prevent growth-sector bias (e.g., Technology vs. Traditional sectors):

Undervalued 🟢: Attractive multiples relative to sector benchmarks (PEG < 1.0 or low P/E + EV/EBITDA).

Fair Value 🟡: Balanced multiples aligned with average sector expectations.

Overvalued 🔴: Elevated multiples exceeding sector thresholds (PEG > 2.0, high P/E or EV/EBITDA).
