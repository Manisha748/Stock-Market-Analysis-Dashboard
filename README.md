
# Ethereum Price Tracker with Airflow & Excel Dashboard

This project automates the daily extraction, transformation, and loading (ETL) of Ethereum (ETH) cryptocurrency price data using Apache Airflow, and visualizes the data dynamically in an Excel dashboard using candlestick charts and other analytics.


## Stock Market Analysis Excel Dashboard

### Dashboard Link :https://github.com/Manisha748/Stock-Market-Analysis-Dashboard/blob/main/stockmarket.xlsx
## Problem Statement
To build an automated system that fetches daily Ethereum (ETH) cryptocurrency prices using Yahoo Finance, stores them in a CSV file, and visualizes the data through a dynamic dashboard in Excel. The system should automatically update data daily using Apache Airflow and support real-time chart refresh in Excel.

## Key Features

### Automated Daily Data Pipeline

- Configured a DAG in **Apache Airflow** to run daily.  
- Fetches **ETH price data** from **Yahoo Finance** using the `yfinance` Python library.  
- Saves the **cleaned data** into a **CSV file** with updated values added each day.

---

###  Data Processing

- Python script processes and transforms **raw financial data**.  
- Ensures consistent column formatting:  
  `Date`, `Open`, `High`, `Low`, `Close`, `Volume`.

---

###  Airflow Integration

- The DAG `eth_price_update_daily` uses a **BashOperator** to trigger a **shell script**.  
- Shell script runs the **data extraction** Python script.  
- **Scheduler** is enabled to automate this task daily without manual intervention.

---

###  Excel Dashboard

- Data is loaded via **Power Query** from the **CSV file** (linked through **WSL**).  
- Built dynamic charts, including Candlestick Charts, to visualize daily ETH price movements.  
- Dashboard automatically refreshes when new data is added by clicking Refresh All.

## Steps followed 

### Data Extraction

Fetch daily ETH-USD prices from Yahoo Finance using the yfinance Python package.

Capture fields like Open, High, Low, Close, Adjusted Close, and Volume.

Save the output in a CSV file.

### Automation with Airflow

Schedule the price-fetching Python script to run daily using Apache Airflow.

Use a BashOperator to run the Python script automatically from a shell script (wrapper.sh).

Ensure the DAG runs daily to append new data.

### Excel Dashboard

Load the CSV file into Excel via Power Query or Data → From Text/CSV.

Create dynamic tables and charts such as candlestick charts and volume trends.

Enable daily refresh via Refresh All to update the dashboard as data changes.

### Integration & Sharing

Store the CSV file in a shared location between WSL and Windows (e.g., /mnt/c/...), then load the data into Excel to create a dynamic stock market analysis dashboard .

## Tools & Technologies:
Apache Airflow (for scheduling)

Python 3.11 (data extraction with yfinance, pandas)

Bash Scripting (to trigger Python from DAG)

Excel Power Query (dynamic data connection)

Excel Charts (Candlestick, Line, and Summary visuals)

WSL (Windows Subsystem for Linux for file management)

# File Description
## eth_tracker/eth.py


Fetches Ethereum (ETH) price data from Yahoo Finance using the yfinance library.

Gets daily historical data (Open, High, Low, Close, Volume).

Saves it to a CSV file named eth_data.csv by appending new data if not already present.

## eth_tracker/wrapper.sh

Bash script that simply runs eth.py.

Airflow’s BashOperator can only run shell commands.

So we use this .sh file to bridge Airflow with Python.


## dags/eth_price_update_daily.py

This is your Airflow DAG file.

Scheduled to run daily, it uses BashOperator to run wrapper.sh, which in turn calls eth.py.

## eth_tracker/eth_data.csv

Stores the Ethereum daily price data in a table format.

Automatically updated every time the DAG runs.

## stockmarket.xlsx

Dynamic Excel dashboard that loads data from eth_data.csv using Power Query.

## Visual Insights 

### Stock Price Trend Analysis (Line Chart)

 Purpose: Helps investors track stock movement over time and identify long-term trends.
 Use Case: If a stock price is consistently rising, it might indicate a good investment opportunity.


<img src="https://github.com/user-attachments/assets/39c260a6-aca9-4319-acca-2dbb71e1c8a9" alt="Chart" width="600"/>





---

### Trading Volume Analysis (Bar Chart)

 Purpose: Shows market activity and interest in a stock.
 Use Case: A sudden increase in volume may indicate strong buying or selling pressure, signaling potential price changes.

 Conditional formatting is used here indicates:

 1) Red for high volume 

 2) Green for low volume 

 High volume may indicate strong buying/selling pressure.

 Low volume may indicate low interest or market stability.

 Helps traders decide when to enter or exit the market.





---

### Stock Volatility Analysis (Price Fluctuations)

 Purpose: Measures how much a stock's price moves up or down.
 Use Case: High volatility means higher risk, while low volatility means stability. Traders use this to decide when to enter or exit trades.

High volatility → Uncertain market conditions (risky trades - red)

 Low volatility → Stable price movement (less risk - green)

Useful for day traders & investors to avoid or take advantage of fluctuations.

---

### Moving Average Crossover Strategy (Buy/Sell Signals)

 Purpose: Helps traders determine the best time to buy or sell stocks.
 Use Case: When the short-term moving average crosses above the long-term moving average, it signals a buy. When it crosses below, it signals a sell.

Conditional Formatting:

Green for "Buy" signals.

Red for "Sell" signals.

Buy when MA10 crosses above MA50 (uptrend starts).

Sell when MA10 crosses below MA50 (downtrend starts).

Helps traders time their entry and exit in the market.



---

### Candlestick Chart (Advanced Visualization)

 Purpose: Helps traders recognize bullish and bearish patterns to predict market direction.
 


<img src="https://github.com/user-attachments/assets/a08fe748-76c0-42f9-801a-c76efb9ba2aa" alt="Chart" width="600"/>


---

### Impact

 Investors – Helps in long-term investment planning.

 Traders – Identifies buy/sell signals for short-term profits.

 Businesses – Analyzes stock market performance for financial planning.
 
 Researchers – Studies stock price movements to develop market strategies.




  


