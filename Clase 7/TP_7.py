## Trabajo de un pipeline de datos + grafica tp8

#Base de datos: Venta de producto A,B,C y D

import pandas as pd
import matplotlib.pyplot as plt

#busco el archivo de datos, sheet name para extraeer los datos de la hoja particular
df= pd.read_excel("Clase 7/ETL_raw_data.xlsx", sheet_name="Inicio")

#guardo en una variable esta columna unica que contiene todo
columna_unica= df.columns[0] 

df_separado= df[columna_unica].str.split(",",expand=True)
# "str" para q interprete cada columna como un texto
# "split" te separará (en la fila) los datos al ver una coma, guardandolos en una lista adentro de la misma columna
# "expand" para separar los elementos de la lista en una columna

#por defecto no agarra la primera fila de datos porque entiende justamente son palabras
#pido con columns, sobreescribir las etiquetas 0,1, que aparecen
df_separado.columns = columna_unica.split(",")

df_separado["Fecha"]=(df_separado["Fecha"]).astype(int) #Guardar fecha como entero

#elimino duplicados
df_separado = df_separado.drop_duplicates()
print(df_separado)


#------- Fin transformación ----
#------- inicio análisis ----

#BuscarV analogo
#traeme de la tabla original solo las filas donde del campo producto diga producto B
df_producto_b= df_separado[df_separado["Producto"] == "Producto B"]

#Si solo quiero los clientes, y sin duplicados pongo
clientes_producto_b = df_producto_b["Cliente"].drop_duplicates()

#Le pone titulo columna
clientes_producto_b = clientes_producto_b.to_frame(name="Cliente x")
print(clientes_producto_b)

#print(df_separado["Valor"].dtype) #lo interpreta tipo str, por ende al sumar, concatena (junta) los valores
#lo paso a numero
df_separado["Valor"] = pd.to_numeric(df_separado["Valor"], errors="coerce")

total_vendido = df_separado["Valor"].sum()
print(f"\n Total Vendimos: {total_vendido}$ dolares")

#---- uso mathlib--- para graficar
ventas_mes = df_separado.groupby("Mes")["Valor"].sum()
plt.plot(ventas_mes.index, ventas_mes.values)
plt.title("Ventas por Mes")
plt.xlabel("Mes")
plt.ylabel("Total Vendido")
plt.show()



