"""
este script muestra el uso de la función info de pandas
"""
import pandas as pd

df = pd.read_csv('../prueba.csv', sep=',')
df.info()
print('stop')
