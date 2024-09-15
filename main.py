### INF601 - Advanced Programming in Python
#### Davon Morris
#### Mini Project 1

import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
import os

mytickers = ["MSFT", "AAPL", "NVDA", "GOOG", "OTGLF"]
mytickers.sort()

mydata = {}
for ticker in mytickers:
    result = yf.Ticker(ticker)
    mydata[ticker] = {'ticker': ticker,
                      'dailyHigh': result.info['dayHigh'],
                      'history': (result.history(period = "1mo"))[-10:],
                      'name': result.info['longName'],
                      }
closing_list = [
    [mydata[ticker]['name'], ticker, mydata[ticker]['history']['Close']]
    for ticker in mytickers
]

# Convert the list to a numpy array
closing_array = np.array(closing_list, dtype=object)

plt.figure(figsize=(10, 6))

# Making charts directory if it doesn't exist
if not os.path.exists("charts/"):
    os.mkdir("charts/")


# Plotting the closing prices for each company in a separate graph
for i in range(len(closing_array)):
    name = closing_array[i][0] # Company Name
    ticker = closing_array[i][1] # Ticker Symbol
    closing_prices = closing_array[i][2] # Closing prices

    # Plot the closing prices
    plt.plot(closing_prices.index,closing_prices.values,label=name)

    # Labels and title for graph
    plt.xlabel("Date") # x-axis
    plt.ylabel("Closing Price (US $)") #y-axis
    plt.title("Closing Prices of Selected Stocks (Last 10 Days)") #Title for graph
    #plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Save the individual plot for the current company
    try:
        plt.savefig(f"charts/{name}_plot.png")
        print(f"{name}_plot.png was created and has been saved to the 'charts' folder.")
    except:
        print(f"{name}_plot.png failed to be created and/or was unable to be saved to the charts folder")


