
import pandas as pd

df = pd.read_csv("/Users/flor/Documents/Facultad/Progra_python/VSC/Clase 8/Citi Bike Trip Data - Sheet1.csv")

# 1. Dimensiones del dataset

print(f"Cantidad de filas: {df.shape[0]}")
print(f"Cantidad de columnas: {df.shape[1]}")

# 2. Columnas y tipos de datos
print("\nColumnas y tipos de datos:")
print(df.dtypes)

# 3. Primeras 5 filas para ver la estructura
print("\nPrimeras 5 filas:")
print(df.head(10))


# 4. Estadísticas descriptivas numéricas (duración, años)
print("\nEstadísticas descriptivas de columnas numéricas:")
#print(df[['birth year']].describe())
print(df[['tripduration']].mean())
print(df[['tripduration']].max())
print(df[['tripduration']].min())

# 5. Cantidad de viajes por género: 
print("\nCantidad de viajes por género:")
print(df['gender'].value_counts())

# 6. Grupo por estación de inicio
grouped_start_station = df.groupby('start station name').size()   #si solo usamos un group by, muestra el conteo de estaciones, size() agrega la cantidad de obs/estacion
print(grouped_start_station)

# 7. Duración media de viaje por género (no)
viajes_por_genero = df.groupby('gender').size()  #sorprendentemente mayor
print(viajes_por_genero)

print("\nDuración media de viaje por género:")
print(df.groupby('gender')['tripduration'].mean())

# 8 Definir un umbral para considerar "viajes largos"
umbral_segundos = 3600

# Filtrar viajes largos y contar por género
viajes_largos = df[df['tripduration'] > umbral_segundos].groupby('gender').size()

print(viajes_largos)


# 8. Cantidad de viajes por estación de inicio
print("\nTop 5 estaciones más usadas como inicio:")
print(df['start station name'].value_counts()) #VALUE COUNTS CUENTA LA CANTIDAD DE ETIQUETAS DIFERENTES

# Asegurarse de que 'starttime' sea datetime
df['starttime'] = pd.to_datetime(df['starttime'], errors='coerce')

# Ahora podés usar .dt.dayofweek sin problemas
df['day_of_week'] = df['starttime'].dt.dayofweek

print("\nDuración media de viaje por día de la semana:")
print(df.groupby('day_of_week')['tripduration'].mean())

# 11. gráficos

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#cantidad de viaje por estacion
plt.figure(figsize=(15, 10))  # Más grande para que se vea mejor
sns.countplot(y='start station name', data=df, order=df['start station name'].value_counts().index)
plt.title('Cantidad de viajes por estación de inicio (todas)')
plt.xlabel('Cantidad de viajes')
plt.ylabel('Estación de inicio')
plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt

# Calcular cantidad de viajes por día (0 = lunes, ..., 6 = domingo)
viajes_por_dia = df.groupby('day_of_week').size()

# Etiquetas de los días en orden
dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']

# Crear el gráfico y guardar el objeto del eje
fig, ax = plt.subplots(figsize=(8, 5))
barras = ax.bar(range(7), viajes_por_dia, color='lightgreen')

# Personalizar el gráfico
ax.set_title('Cantidad de viajes por día de la semana')
ax.set_xlabel('Día de la semana')
ax.set_ylabel('Cantidad de viajes')
ax.set_xticks(range(7))
ax.set_xticklabels(dias, rotation=45)
ax.grid(axis='y')

# Agregar etiquetas numéricas sobre cada barra
for i, barra in enumerate(barras):
    altura = barra.get_height()
    ax.text(barra.get_x() + barra.get_width()/2, altura + 100, str(altura),
            ha='center', va='bottom', fontsize=9)

plt.tight_layout()
plt.show()


dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']

plt.figure(figsize=(8,8))
plt.pie(viajes_por_dia, labels=dias, autopct='%1.1f%%', startangle=90, colors=plt.cm.Pastel1.colors)
plt.title('Porcentaje de viajes por día de la semana')
plt.axis('equal')  # Para que quede circular
plt.show()



