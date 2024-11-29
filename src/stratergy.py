import pandas as pd
from options_data import calculate_option_premium

def calculate_max_profit(short_premium: float, long_premium: float) -> float:
    """
    Calculate the max profit from the strategy.
    Max profit occurs when BTC is near the strike price at the time of short option expiry.
    """

    # log max profit
    # print(f"short_premium: {short_premium}, long_premium: {long_premium}")
    # print(f"max profit: {long_premium -short_premium}")
    return  long_premium - short_premium # Corrected to reflect that max profit is short_premium - long_premium

def calculate_max_loss(short_premium: float, long_premium: float) -> float:
    """
    Calculate the max loss from the strategy.
    Max loss occurs when the price moves significantly away from the strike price.
    """
    # log max loss
    # print(f"short_premium: {short_premium}, long_premium: {long_premium}")
    # print(f"max loss: { short_premium -long_premium}")
    return  short_premium -long_premium # Corrected to reflect that max loss is long_premium - short_premium

def calculate_apy(monthly_profit: float, initial_investment: float) -> float:
    """
    Calculate the annualized percentage yield (APY) from the monthly profit.
    """

    # log APY
    # print(f"monthly_profit: {monthly_profit}, initial_investment: {initial_investment}")
    # print(f"APY: {(1 + (monthly_profit / initial_investment)) ** 12 - 1}")

    return (1 + (monthly_profit / initial_investment)) ** 12 - 1


def simulate_calendar_spread(btc_data: pd.DataFrame, strike_price: float, long_expiry_days: int, short_expiry_days: int, volatility: float) -> pd.DataFrame:
    """
    Simulate the gamma-neutral calendar spread strategy over a range of Bitcoin price movements.
    """
    monthly_results = []
    
    for index, row in btc_data.iterrows():
        price = row['Close']

        # Calculate option premiums
        long_premium = calculate_option_premium(price, strike_price, long_expiry_days / 365, volatility, is_call=True)
        short_premium = calculate_option_premium(price, strike_price, short_expiry_days / 365, volatility, is_call=True)

        # Max Profit and Max Loss
        monthly_profit = 0
        if short_premium < long_premium:
            short_premium, long_premium = short_premium, long_premium
            monthly_profit =  long_premium -short_premium # Simplified assumption; adjust for real decay
        else:
            short_premium, long_premium = long_premium, short_premium
            monthly_profit = short_premium - long_premium  # Simplified assumption; adjust for real decay
        

        max_profit = calculate_max_profit(short_premium, long_premium)
        max_loss = calculate_max_loss(short_premium, long_premium)

        # Assume monthly profit based on option premium decay (simplified for example)
        
        # print(f"Monthly Profit: {monthly_profit}")
        # # log long premium
        # print(f"long_premium: {long_premium}")
        # Calculate APY
        apy = calculate_apy(monthly_profit, long_premium)
        print('APY:', apy)

        monthly_results.append({
            'Date': index,
            'BTC_Price': price,
            'Max_Profit': max_profit,
            'Max_Loss': max_loss,
            'Monthly_Profit': monthly_profit,
            'APY': apy
        })

    return pd.DataFrame(monthly_results)  