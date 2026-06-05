#Modelo de regresión lineal - aprendisaje supervisado

# Paso 1: Importar librerías
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Paso 2: Datos de ejemplo
# Entrada (x) y salida (y)
x = np.array([1, 2, 3, 4, 8]).reshape(-1, 1)    #horas de estudio #Scikit-learn siempre espera que las variables de entrada (x) sean una matriz 2D, incluso si solo hay una columna. [[1],[2],[3],[4],[8]]
y = np.array([2, 4, 5, 4, 6])                   #notas de examen

# Paso 3: Crear y entrenar el modelo
modelo = LinearRegression()       # el modelo lo creamos usando regresión lineal con nuestros datos
modelo.fit(x, y)

# Paso 4: Predecir
x_pred = np.array([[6]])  # ¿Qué pasa cuando x = 6?
y_pred = modelo.predict(x_pred) #predicción (modelo)

print(f"Predicción para x = 6: y = {y_pred[0]:.2f}")    # lo que hace el modelo es crear una función que predicev

# Paso 5: Visualizar
plt.scatter(x, y, color='blue', label='Datos reales')
plt.plot(x, modelo.predict(x), color='red', label='Modelo')
plt.scatter(x_pred, y_pred, color='green', label='Predicción x=6')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Regresión Lineal Simple')
plt.legend()
plt.grid(True)
plt.show()
