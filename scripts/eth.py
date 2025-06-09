import yfinance as yf
import pandas as pd
from datetime import datetime

start_date = "2025-01-01"
end_date =  datetime.today().strftime('%Y-%m-%d')

print(f"Fetching ETH data from {start_date} to {end_date}")
data = yf.download("ETH-USD", start=start_date, end=end_date, group_by='ticker', auto_adjust=False)

# Flatten multi-index columns
data.columns = ['_'.join(col).strip() if col[1] else col[0] for col in data.columns]

# Reset index to bring 'Date' into a column
data.reset_index(inplace=True)

# Print column names
print("Flattened columns:", data.columns.tolist())

# Select the necessary columns
desired_cols = ['Date', 'ETH-USD_Open', 'ETH-USD_High', 'ETH-USD_Low',
                'ETH-USD_Close', 'ETH-USD_Adj Close', 'ETH-USD_Volume']
available_cols = [col for col in desired_cols if col in data.columns]

# Filter DataFrame
data = data[available_cols]

# Rename for consistency
data.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume'][:len(available_cols)]

# Show result
print(data.head())
data.to_csv("/home/robert_manisha/airflow_project/eth_tracker/eth_data.csv", index=False)
