import pandas as pd
import matplotlib.pyplot as plt

file_path = "datos.csv"
df = pd.read_csv(file_path, encoding="latin-1")

# Corregir el nombre de la columna
df.rename(columns={'AÃ±o_EVA': 'Año_EVA'}, inplace=True)

# Mostrar primeras filas del DataFrame
print(df.head())

# Mostrar información sobre el DataFrame
print(df.info())

# Descripción estadística básica
print(df.describe())

# Estadísticas de las columnas de los meses
meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
print(df[meses].describe())

#Revisar si hay valores nulos
print(df.isnull().sum())

# Sumar las producciones mensuales de todos los cultivos
produccion_mensual = df[meses].sum()

# Crear gráfico de líneas para mostrar la producción total por mes
ax = produccion_mensual.plot(kind='line', marker='o', figsize=(10, 6))
plt.title('Producción Mensual Total')
plt.xlabel('Mes')
plt.ylabel('Producción Total')
plt.grid(True)

# Guardar el gráfico como archivo JPG
plt.savefig("produccion_mensual_total.jpg")

# Cerrar la figura actual para evitar que se sobrepongan gráficos
plt.close()

# Crear un boxplot para visualizar la distribución de la producción en cada mes
ax = df[meses].plot(kind='box', figsize=(10, 6))
plt.title('Distribución de Producción Mensual')
plt.ylabel('Producción')

# Guardar el gráfico como archivo PNG
plt.savefig("distribucion_produccion_mensual.png")

# Cerrar la figura actual para evitar que se sobrepongan gráficos
plt.close()
