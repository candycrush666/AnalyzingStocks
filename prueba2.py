import pandas as pd
import requests
from bs4 import BeautifulSoup

# URL de la página web que contiene los datos de ingresos de Tesla
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"

# Realizar la solicitud GET para obtener el contenido de la página web
response = requests.get(url)

# Crear el objeto BeautifulSoup para analizar el contenido HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Encontrar la tabla que contiene los datos de ingresos de Tesla
table = soup.find('table')

# Extraer los datos de la tabla y guardarlos en un DataFrame
tesla_revenue = pd.read_html(str(table))[0]

# Cambiar el nombre de las columnas
tesla_revenue.columns = ['Date', 'Revenue']

# Eliminar la coma y el signo de dólar de la columna de ingresos
tesla_revenue["Revenue"] = tesla_revenue['Revenue'].str.replace(',|\$',"")

# Eliminar filas con valores nulos o cadenas vacías en la columna de ingresos
tesla_revenue.dropna(inplace=True)
tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]

# Mostrar las últimas cinco filas del DataFrame
print(tesla_revenue.tail())
