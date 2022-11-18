"""
Lineas de código que permiten ejecutar un cambio de nombre en
un dataframe leido previamente con pandas
"""
import pandas as pd

df = pd.read_csv('../prueba.csv', sep=',')
df.rename(columns={'registrados': 'register'}, inplace=True)

