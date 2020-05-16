import pandas as pd
import matplotlib.pyplot as plt #biblioteca para graficar
import seaborn as sns #biblioteca para graficar
#############################################################################
print("Hello World")
print("Ensayo 2")
print("5")
datos=pd.read_csv("CovidCol.csv",header=0)
print (datos)
print("_-----_")
print(datos.head())
df=pd.DataFrame(datos)
df.groupby("atención")["Edad"].mean().plot(kind="bar",legend="reverse")
df.columns.values
#print(df.describe(datos)) #esto muestra estad basicas
print (df.columns.values)
