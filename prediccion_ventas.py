import pandas as pd

file_path = "datos.csv"
df = pd.read_csv(file_path, encoding="latin-1")

# Corregir el nombre de la columna
df.rename(columns={'AÃ±o_EVA': 'Año_EVA'}, inplace=True)