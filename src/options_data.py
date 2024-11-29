import yfinance as yf
import pandas as pd

def fetch_bitcoin_data(start_date: str, end_date: str) -> pd.DataFrame:
    """
    Fetch Bitcoin historical price data from Yahoo Finance.
    """
    # Use yfinance to fetch Bitcoin data
    btc_data = yf.download("BTC-USD", start=start_date, end=end_date)
    # btc_data = yf.download("NFLX", start=start_date, end=end_date)
    # print btc data 
    print(btc_data)
    return btc_data

def calculate_option_premium(price: float, strike: float, time_to_expiry: float, volatility: float, is_call: bool) -> float:
    """
    Calculate the option premium using a simplified Black-Scholes model for calls and puts.
    """
    from math import log, sqrt, exp
    from scipy.stats import norm
    
    # Black-Scholes Model
    d1 = (log(price / strike) + (0.5 * volatility ** 2) * time_to_expiry) / (volatility * sqrt(time_to_expiry))
    d2 = d1 - volatility * sqrt(time_to_expiry)
    
    if is_call:
        # Call Option Price
        option_price = price * norm.cdf(d1) - strike * exp(-0.05 * time_to_expiry) * norm.cdf(d2)
    else:
        # Put Option Price
        option_price = strike * exp(-0.05 * time_to_expiry) * norm.cdf(-d2) - price * norm.cdf(-d1)
    
    return option_price 