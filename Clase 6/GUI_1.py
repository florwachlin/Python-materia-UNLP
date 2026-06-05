import tkinter as tk

# función que se ejecuta al apretar el botón
def saludar():
    nombre = entrada.get()  # obtiene lo que escribió el usuario
    resultado.config(text=f"Hola {nombre}")  # actualiza el texto de la etiqueta resultado con el saludo personalizado. config() es un método que permite cambiar las propiedades de un widget, en este caso el texto que se muestra en la etiqueta resultado. Cada vez que se llama a saludar(), se actualiza el texto con el nuevo nombre ingresado por el usuario.

# crear ventana
ventana = tk.Tk()
ventana.title("Mi primera GUI")

# texto fijo (no cambia)
titulo = tk.Label(ventana, text="Escribí tu nombre:")
titulo.pack() #pack es un método que organiza los elementos en la ventana, en este caso los apila verticalmente. Hay otros métodos como grid() o place() para organizar de otras formas.

# campo de entrada
entrada = tk.Entry(ventana) #solamente crea el campo de entrada, no lo muestra. Para mostrarlo, usamos pack() o algún otro método de organización.
entrada.pack()

# # botón
boton = tk.Button(ventana, text="Saludar", command=saludar)
boton.pack()

# # texto que cambia
resultado = tk.Label(ventana, text="")
resultado.pack()

# ejecutar la app
ventana.mainloop()