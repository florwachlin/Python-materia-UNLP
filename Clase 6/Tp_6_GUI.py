#Trabajo 5

#Crear una ventana gráfica donde el usuario pueda elegir entre un menu de funciones

import tkinter as tk
from tkinter import messagebox
import hashlib
import math
import random


ventana = tk.Tk()
ventana.title("Sistema con login: ")
ventana.geometry("300x250")

#genero hash
def generar_hash(texto):
    return hashlib.sha256(texto.encode()).hexdigest()
#encode y me pasa el texto a binario


#python123
hash_correcto= "a8a15faedf1420db2b80e81fe86167d785aaafb2c4da29bc55637ac1de7751d9"

intentos = 0
def verificar():
    global intentos #voy a modificar la variable global de intentos (sino la cambia solo localmente)
    
    contra_ingresa= entrada_pass.get() #ingresa lo del bloque y lo guarda en esta variable

    if generar_hash(contra_ingresa) == hash_correcto:
        messagebox.showinfo("Ok", "Bienvenido")
        mostrar_menu()

    else:
        intentos+=1
        messagebox.showinfo("Error", f"Intentos realizados {intentos}/3") #analogo al print

        if intentos >=3:
            messagebox.showerror("Bloqueado","Acceso denegado") #analogo al print
            ventana.destroy() #cerrará esta ventana

#---- funciones del sistema
def numero_random():
    messagebox.showinfo("Random", str(random.randint(1, 100)))

def raiz():
    try:
        num = float(entrada_num.get())
        messagebox.showinfo("Raiz: ", str(math.sqrt(num)))
    except:
        messagebox.showinfo("Error", "Numero inválido")

def mensaje():
    messagebox.showinfo("Mensaje", "Hola desde la GUI")

#--- Cambio a menú

def mostrar_menu():
    frame_login.pack_forget()
    frame_menu.pack

#frames/ bloques donde contendra datos: boton, letras
frame_login = tk.Frame(ventana)
frame_menu = tk.Frame(ventana)

#loginnn
tk.Label(frame_login, text= "Ingresar") 
#label hace... dentro de la variable frame_login, lo siguiente)
#bloque dirá texto ingresar. 

entrada_pass= tk.Entry(frame_login, show= "*") #tendra una caja de texto donde podra completar
#el usuario
entrada_pass.pack()

#dps aparezca un boton 
tk.Button(frame_login, text="Ingresar", command=verificar ).pack()
frame_login.pack()

# -- menu 
def mostrar_menu():
    frame_login.pack_forget()
    frame_menu.pack()

tk.Button(frame_menu, text="Número random", command=numero_random).pack()
tk.Button(frame_menu, text="Mensaje", command=mensaje).pack()

tk.Label(frame_menu, text="Numero para raiz:").pack()
entrada_num =tk.Entry(frame_menu)
entrada_num.pack()

tk.Button(frame_menu, text= "calcular raiz", command=raiz).pack()
tk.Button(frame_menu, text="salir", command=ventana.destroy).pack()

ventana.mainloop()