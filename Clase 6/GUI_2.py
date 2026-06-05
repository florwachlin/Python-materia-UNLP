import tkinter as tk

#aclaración 1: usaremos get() para obtener el valor de las entradas: nombre = entrada_nombre.get() análogo al input para los programas en consola
# get() siempre devuelve un string, por eso en la función sumar() convertimos a float para poder operar con números. Para mostrar el resultado o mensajes de error, usamos el método config() de la etiqueta resultado: resultado.config(text="Texto a mostrar"). Esto actualiza el texto que se muestra en la etiqueta cada vez que se llama a la función asociada al botón.
#aclaración 2: config() para actualizar el texto de la etiqueta resultado. Es como el 'print' pero para la GUI, ya que no tenemos una consola para mostrar resultados. Cada vez que se llama a la función asociada al botón, se actualiza el texto de la etiqueta resultado con el nuevo mensaje o resultado de la operación.

def saludar():
    nombre = entrada_nombre.get()
    if nombre == "":
        resultado.config(text="Escribí tu nombre")
    else:
        resultado.config(text=f"Hola {nombre} 👋") 

def sumar():
    try:
        n1 = float(entrada_num1.get())
        n2 = float(entrada_num2.get())
        resultado.config(text=f"Resultado: {n1 + n2}")
    except:
        resultado.config(text="Ingresá números válidos")

# Ventana principal
ventana = tk.Tk()
ventana.title("Mi primera GUI")
ventana.geometry("300x250")

# Nombre
tk.Label(ventana, text="Nombre:").pack()
entrada_nombre = tk.Entry(ventana)
entrada_nombre.pack()

tk.Button(ventana, text="Saludar", command=saludar).pack()

# Separador
tk.Label(ventana, text="-----------").pack()

# Suma
tk.Label(ventana, text="Número 1:").pack()
entrada_num1 = tk.Entry(ventana)
entrada_num1.pack()

tk.Label(ventana, text="Número 2:").pack()
entrada_num2 = tk.Entry(ventana)
entrada_num2.pack()

tk.Button(ventana, text="Sumar", command=sumar).pack()

# Resultado
resultado = tk.Label(ventana, text="")
resultado.pack()

ventana.mainloop()