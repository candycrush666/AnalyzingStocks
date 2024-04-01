import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Obtener datos de acciones de Tesla
tesla_data = yf.download("TSLA")

# Definir la función make_graph
def make_graph(stock_data, title):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing = .3)
    fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['Close'], name="Share Price"), row=1, col=1)
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_layout(title=title, xaxis_rangeslider_visible=True)
    fig.show()

# Graficar los datos de las acciones de Tesla
make_graph(tesla_data, title="Tesla Stock Data")
