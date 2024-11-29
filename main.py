import pandas as pd
import sys
import os
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.dates import DateFormatter

# Add the 'src' directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

# Import the functions from your strategy files
from options_data import fetch_bitcoin_data
from stratergy import simulate_calendar_spread
from utils import days_to_expiry

def plot_results(results: pd.DataFrame):
    """
    Plot the results of the Gamma-Neutral Calendar Spread strategy.
    """
    if results.empty:
        print("No results to plot.")
        return

    # Convert Date column to datetime
    results['Date'] = pd.to_datetime(results['Date'])

    # Set up the plotting environment
    sns.set(style="whitegrid")
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # Date format for the x-axis
    date_format = DateFormatter("%b-%Y")  # Example: Jan-2024

    # Plot 1: BTC Price over time
    axes[0, 0].plot(results['Date'], results['BTC_Price'], color='blue', label='BTC Price')
    axes[0, 0].set_title('Bitcoin Price Over Time', fontsize=14, weight='bold')
    axes[0, 0].set_xlabel('')
    axes[0, 0].set_ylabel('BTC Price (USD)', fontsize=12)
    axes[0, 0].legend()
    axes[0, 0].xaxis.set_major_formatter(date_format)
    axes[0, 0].tick_params(axis='x', rotation=45)

    # Plot 2: Max Profit and Max Loss over time
    axes[0, 1].plot(results['Date'], results['Max_Profit'], color='green', label='Max Profit', linewidth=2)
    axes[0, 1].plot(results['Date'], results['Max_Loss'], color='red', label='Max Loss', linewidth=2)
    axes[0, 1].set_title('Max Profit and Max Loss Over Time', fontsize=14, weight='bold')
    axes[0, 1].set_xlabel('')
    axes[0, 1].set_ylabel('Profit/Loss (USD)', fontsize=12)
    axes[0, 1].legend()
    axes[0, 1].xaxis.set_major_formatter(date_format)
    axes[0, 1].tick_params(axis='x', rotation=45)

    # Plot 3: Monthly Profit over time
    axes[1, 0].bar(results['Date'], results['Monthly_Profit'], color='teal', alpha=0.7, label='Monthly Profit')
    axes[1, 0].set_title('Monthly Profit Over Time', fontsize=14, weight='bold')
    axes[1, 0].set_xlabel('')
    axes[1, 0].set_ylabel('Monthly Profit (USD)', fontsize=12)
    axes[1, 0].legend()
    axes[1, 0].xaxis.set_major_formatter(date_format)
    axes[1, 0].tick_params(axis='x', rotation=45)

    # Plot 4: APY over time
    axes[1, 1].plot(results['Date'], results['APY'], color='purple', label='APY', linewidth=2)
    axes[1, 1].set_title('Annualized Percentage Yield (APY) Over Time', fontsize=14, weight='bold')
    axes[1, 1].set_xlabel('Date', fontsize=12)
    axes[1, 1].set_ylabel('APY (%)', fontsize=12)
    axes[1, 1].legend()
    axes[1, 1].xaxis.set_major_formatter(date_format)
    axes[1, 1].tick_params(axis='x', rotation=45)

    plt.tight_layout()
    plt.show()

def main():
    # Define parameters
    start_date = '2024-01-01'
    end_date = '2024-11-30'
    strike_price = 1000  # Example strike price for BTC options
    long_expiry_days = 365  # 1 year for the long position
    short_expiry_days = 30  # 1 month for the short position
    volatility = 0.6  # Assume a volatility of 60% for Bitcoin

    # Fetch Bitcoin data from Binance
    btc_data = fetch_bitcoin_data(start_date, end_date)

    # Simulate the calendar spread strategy
    results = simulate_calendar_spread(btc_data, strike_price, long_expiry_days, short_expiry_days, volatility)

    # Plot the results
    plot_results(results)

if __name__ == "__main__":
    main()
