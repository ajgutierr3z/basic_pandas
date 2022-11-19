"""
Lineas de código que permiten ejecutar agregar
una columna a un dataframe previamente cargado
"""
import pandas as pd

df = pd.read_csv('../prueba.csv', sep=',')
df.rename(columns={'registrados': 'register'}, inplace=True)
df['Registrados'] = df['register']


