"""
Lineas de código que muestran el uso de head y tail
con pandas
"""
import pandas as pd


df = pd.read_csv('../prueba.csv', sep=',')
df.head(5)
df.tail(5)
print('stop')
