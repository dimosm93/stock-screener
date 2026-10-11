import streamlit as st
from data_processor import create_stock_dataframe

# Page Configuration
st.set_page_config(page_title="Stock Screener", layout="wide")

st.title(" Stock Screener & Fundamental Valuation")
st.markdown("Enter stock symbols to analyze:")

# User Input for stock tickers
user_input = st.text_input("Tickers (comma separated):", "AAPL, MSFT, NVDA, TSLA")

# Execution Button
if st.button("Run Screener"):
    # Convert input string into a cleaned list of ticker symbols
    ticker_list = [symbol.strip().upper() for symbol in user_input.split(",") if symbol.strip()]
    
    with st.spinner("Fetching data from Yahoo Finance..."):
        df = create_stock_dataframe(ticker_list)
        
        if not df.empty:
            st.success(f"Successfully fetched data for {len(df)} stocks!")
            st.dataframe(df, use_container_width=True)
        else:
            st.error("No valid data found for the provided tickers.")