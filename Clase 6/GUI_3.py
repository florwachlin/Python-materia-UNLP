import tkinter as tk
from tkinter import messagebox

def mostrar_info():
    messagebox.showinfo("Info", "Esta es una app de ejemplo")

# ventana principal
ventana = tk.Tk()
ventana.title("App con menú")

# crear barra de menú
barra_menu = tk.Menu(ventana)

# menú Archivo
menu_archivo = tk.Menu(barra_menu, tearoff=0)
menu_archivo.add_command(label="Salir", command=ventana.quit)

# menú Ayuda
menu_ayuda = tk.Menu(barra_menu, tearoff=0)
menu_ayuda.add_command(label="Acerca de", command=mostrar_info)

# agregar menús a la barra
barra_menu.add_cascade(label="Archivo", menu=menu_archivo)
barra_menu.add_cascade(label="Ayuda", menu=menu_ayuda)

# configurar la ventana para que use el menú
ventana.config(menu=barra_menu)

ventana.mainloop()
