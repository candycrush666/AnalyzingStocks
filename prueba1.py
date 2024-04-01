import yfinance as yf

# Use yfinance to extract Tesla stock data
tesla_data = yf.download('TSLA', period='max')

# Reset the index
tesla_data.reset_index(inplace=True)

# Display the first five rows
print(tesla_data.head())
