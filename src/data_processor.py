from data_fetcher import get_raw_stock_info

def clean_stock_data(raw_info: dict) -> dict:
    """
    Cleans and transforms raw financial data from yfinance into a 
    standardized dictionary containing essential financial metrics.
    
    :param raw_info: Raw dictionary returned by yfinance Ticker.info
    :return: Cleaned dictionary with normalized key names
    """
    # Guard clause: Return an empty dictionary if raw_info is empty or invalid
    if not raw_info:
        return {}

    # Extract and normalize fundamental financial metrics
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


if __name__ == "__main__":
    # Test data processing with Microsoft (MSFT)
    symbol = "MSFT"
    print(f"--- Fetching & Processing Data for {symbol} ---")
    
    # 1. Fetch raw stock data
    raw_data = get_raw_stock_info(symbol)
    
    # 2. Clean and normalize data
    processed_data = clean_stock_data(raw_data)
    
    # 3. Print processed key-value pairs
    for key, value in processed_data.items():
        print(f"{key}: {value}")