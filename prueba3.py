import yfinance as yf

# Utilizar yfinance para extraer datos de acciones de GameStop (GME)
gme_data = yf.download("GME", period="max")

# Reiniciar el índice del DataFrame
gme_data.reset_index(inplace=True)

# Mostrar las primeras cinco filas del DataFrame
print(gme_data.head())
