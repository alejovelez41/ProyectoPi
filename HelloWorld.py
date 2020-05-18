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
df.groupby("atención")["Edad"].count().plot(kind="bar",legend="reverse")
df.columns.values
#df.plot("atención", "Edad", kind="bar",legend="reverse")

#print(df.describe(datos)) #esto muestra estad basicas
print (df.columns.values)
print ("la edad promedio es ",df.Edad.mean())
print(df.pivot_table("Edad", "atención"))
print(df.pivot_table("ID de caso", "Departamento o Distrito ", "atención", aggfunc ="count", margins="true"))
#my_plot = datos.plot("Edad", "atención", kind="scatter")
#plt.show()
#plt.plot("Edad","atención")
#plt.show("Edad","atención")
#plt.ion("Edad","atención") #es como el .show pero mejor
#plt.plot([1, 2, 3, 4])
#plt.ylabel('some numbers')

plt.show() #esta funciona