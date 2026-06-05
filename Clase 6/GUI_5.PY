import tkinter as tk
from tkinter import messagebox
import hashlib
import random
import math

# --- HASH ---
def generar_hash(texto):
    return hashlib.sha256(texto.encode()).hexdigest()

HASH_CORRECTO = "a8a15faedf1420db2b80e81fe86167d785aaafb2c4da29bc55637ac1de7751d9"

# --- Ventana principal ---
ventana = tk.Tk()
ventana.title("Sistema con login")
ventana.geometry("300x250")

# --- Variables ---
intentos = 0

# --- LOGIN ---
def verificar():
    global intentos

    contra = entrada_pass.get()
    if generar_hash(contra) == HASH_CORRECTO:
        messagebox.showinfo("OK", "Bienvenido!")
        mostrar_menu()
    else:
        intentos += 1
        messagebox.showwarning("Error", f"Intento {intentos}/3")

        if intentos >= 3:
            messagebox.showerror("Bloqueado", "Acceso denegado")
            ventana.destroy()

# --- FUNCIONES DEL SISTEMA ---
def numero_random():
    messagebox.showinfo("Random", str(random.randint(1, 100)))

def raiz():
    try:
        num = float(entrada_num.get())
        messagebox.showinfo("Raíz", str(math.sqrt(num)))
    except:
        messagebox.showerror("Error", "Número inválido")

def mensaje():
    messagebox.showinfo("Mensaje", "Hola desde la GUI 😎")

# --- CAMBIO A MENÚ ---
def mostrar_menu():
    frame_login.pack_forget()
    frame_menu.pack()

# --- FRAMES ---
frame_login = tk.Frame(ventana)
frame_menu = tk.Frame(ventana)

# --- LOGIN UI ---
tk.Label(frame_login, text="Contraseña:").pack()

entrada_pass = tk.Entry(frame_login, show="*")
entrada_pass.pack()

tk.Button(frame_login, text="Ingresar", command=verificar).pack()

frame_login.pack()

# --- MENU UI ---
tk.Button(frame_menu, text="Número random", command=numero_random).pack()
tk.Button(frame_menu, text="Mensaje", command=mensaje).pack()

tk.Label(frame_menu, text="Número para raíz:").pack()

entrada_num = tk.Entry(frame_menu)
entrada_num.pack()

tk.Button(frame_menu, text="Calcular raíz", command=raiz).pack()

tk.Button(frame_menu, text="Salir", command=ventana.destroy).pack()

# --- LOOP ---
ventana.mainloop()