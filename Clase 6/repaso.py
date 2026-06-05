import hashlib
import getpass
import time
import random
import math

# --- Hash ---
def generar_hash(texto):
    return hashlib.sha256(texto.encode()).hexdigest()

HASH_CORRECTO = "a8a15faedf1420db2b80e81fe86167d785aaafb2c4da29bc55637ac1de7751d9"

# --- Login ---
def verificar_contraseña():
    intentos = 0

    while intentos < 3:
        contra = getpass.getpass("Ingresá la contraseña: ")
        if generar_hash(contra) == HASH_CORRECTO:
            print("Contraseña correcta. Bienvenido!\n")
            return True
        else:
            intentos += 1
            print(f"Incorrecta. Intento {intentos}/3")
            time.sleep(1)

    print("Acceso denegado.")
    return False

# --- Funciones “boludas” ---
def numero_random():
    print("Número random:", random.randint(1, 100))

def raiz():
    num = float(input("Número: "))
    print("Raíz:", math.sqrt(num))

def mensaje():
    print("Hola mundo desde el sistema 😎")

# --- Menú ---
def mostrar_menu():
    print("\n--- MENÚ ---")
    print("1. Número random")
    print("2. Raíz cuadrada")
    print("3. Mensaje")
    print("4. Salir")

# --- Programa principal ---
if verificar_contraseña():

    while True:
        mostrar_menu()
        opcion = input("Elegí una opción: ")

        if opcion == "1":
            numero_random()
        elif opcion == "2":
            raiz()
        elif opcion == "3":
            mensaje()
        elif opcion == "4":
            print("Saliendo...")
            break
        else:
            print("Opción inválida")