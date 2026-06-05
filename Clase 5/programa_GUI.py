import tkinter as tk
from tkinter import messagebox
import hashlib
import math

#python123
hash_verdadero = "a8a15faedf1420db2b80e81fe86167d785aaafb2c4da29bc55637ac1de7751d9"

def generar_hash(entrada):
    return hashlib.sha256(entrada.encode()).hexdigest()

# funciones menu
def mensaje():
    messagebox.showinfo(frame_menu,"Bienvenido")

def cos_rad():
    frame_menu.pack_forget()
    frame_coseno.pack()

    angulo_rad= angulo_entrada.get()

    if "," in angulo_rad: #solo cambio coma con puntos
        angulo_rad= angulo_rad.replace(",",".")
    
    #si tiene palabra . palabra ... cuando pruebe pasarlo a float, no te dejaria
    try:
        angulo_rad = float(angulo_rad)
        cos_angulo = math.cos(angulo_rad)
        print(cos_angulo)
    except:
        print("Formato incorrecto")
        return None

    return(cos_angulo) 

def mostrar_menu():
    frame_login.pack_forget() #elimino de la visual el login
    frame_menu.pack() #empeza a motrarse el bloque del menu


intentos=0
def verificar():
    global intentos #si yo no lo pongo interpreta es una variable externa que nunca puede cambiar
    
    entrada = entrada_usuario.get() #Lo que escriba en el bloque será lo que se llamará "entrada" 
    #variable entrada funcion
    if generar_hash(entrada) == hash_verdadero:
        mostrar_menu() #el while true no te sirve
        #porque en la pantalla vas a ver siempre el frame del menu
    
    else:
        messagebox.showinfo("Contraseña incorrecta",f"Intentos realizados {intentos}/3")
        intentos+=1


#ventana principal
ventana = tk.Tk()
ventana.geometry("300x250")
ventana.title("Mi primer programa con interfaz gráfica")

frame_login = tk.Frame(ventana)
frame_login.pack()
#la ventana tendra un bloque VISUAL que será del login iniciar

tk.Label(frame_login, text="Bienvenido al programa").pack()
tk.Label(frame_login, text= "ingrese su contraseña").pack()

entrada_usuario = tk.Entry(frame_login, show="*")
entrada_usuario.pack()
boton = tk.Button(frame_login, text="ingresar", command=verificar).pack() #######

frame_menu = tk.Frame(ventana) 
#dentro de la ventana genero un frame OCULTO

tk.Label(frame_menu, text= "Elige una opcion").pack()
tk.Button(frame_menu,text= "Saludo", command=mensaje).pack()

tk.Button(frame_menu, text="Calcular el coseno de un angulo (rad)",command=cos_rad).pack()

frame_coseno = tk.Frame(frame_menu) #convive un frame en el menu

tk.Label(frame_coseno, text="Calcular el coseno de un angulo (rad)").pack()
angulo_entrada = tk.Entry(frame_coseno, text="Numero en rad")
angulo_entrada.pack()

tk.Button(frame_coseno,text="Coseno angulo",command=cos_rad).pack()


ventana.mainloop()

