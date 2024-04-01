import requests
import pandas as pd
from bs4 import BeautifulSoup

# Paso 1: Descargar la página web
url = "https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue"
html_data = requests.get(url).text

# Paso 2: Parsear los datos HTML
soup = BeautifulSoup(html_data, "html.parser")

# Paso 3: Extraer la tabla de ingresos de GameStop
gme_revenue = pd.DataFrame(columns=['Date', 'Revenue'])

# Buscamos todas las etiquetas tbody
for tbody in soup.find_all("tbody"):
    # Verificamos si la tabla contiene al menos dos filas (Date y Revenue)
    rows = tbody.find_all("tr")
    if len(rows) > 1:
        for row in rows:
            col = row.find_all("td")
            date = col[0].text
            revenue = col[1].text.replace("$", "").replace(",", "")

            gme_revenue = gme_revenue.append({"Date": date, "Revenue": revenue}, ignore_index=True)
        break  # Salimos del bucle si encontramos la tabla

# Paso 4: Mostrar las últimas cinco filas de los ingresos de GameStop
print(gme_revenue.tail())


