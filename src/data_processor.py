import pandas as pd
from data_fetcher import get_raw_stock_info

def clean_stock_data(raw_info: dict) -> dict:
    """
    Cleans and transforms raw financial data from yfinance into a 
    standardized dictionary containing essential financial metrics.
    """
    if not raw_info:
        return {}

    cleaned_data = {
        'symbol': raw_info.get('symbol'),
        'name': raw_info.get('longName') or raw_info.get('shortName') or 'N/A',
        'price': raw_info.get('currentPrice') or raw_info.get('regularMarketPrice'),
        'pe_ratio': raw_info.get('trailingPE'),
        'peg_ratio': raw_info.get('pegRatio'),
        'ev_ebitda': raw_info.get('enterpriseToEbitda'),
        'sector': raw_info.get('sector', 'N/A'),
        'market_cap': raw_info.get('marketCap')
    }

    return cleaned_data


def create_stock_dataframe(tickers: list) -> pd.DataFrame:
    """
    Fetches, cleans, and consolidates financial data for multiple tickers
    into a  Pandas DataFrame.
    """
    processed_list = []
    
    for symbol in tickers:
        raw_data = get_raw_stock_info(symbol)
        cleaned_data = clean_stock_data(raw_data)
        
        
        if cleaned_data:
            processed_list.append(cleaned_data)
            
    # Convert list of dictionaries into a Pandas DataFrame
    df = pd.DataFrame(processed_list)
    return df


if __name__ == "__main__":
    # Test multi-stock processing including an invalid ticker
    test_tickers = ["AAPL", "MSFT", "NVDA", "INVALID_TICKER"]
    print(f"--- Fetching & Building DataFrame for: {test_tickers} ---")
    
    df_stocks = create_stock_dataframe(test_tickers)
    
    print("\nResulting DataFrame:")
    print(df_stocks.to_string())