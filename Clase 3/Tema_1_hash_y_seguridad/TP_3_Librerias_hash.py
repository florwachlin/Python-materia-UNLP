#TEMA USO LIBRERIA 

import math
print(math.sqrt(4)) # te da la raiz cuadrada de 4
print(math.pi) # no me demando un argumento 

#-----#

#TEMA SEGURIDAD

import hashlib
import getpass #para ocultar la contraseña por pantalla q ingresa el usuario

contraseña = getpass.getpass("Ingrese su contraseña") # debe ser tipo string, lo cual
#lo guarda asi, asiq bienF

contraseña_binaria = contraseña.encode() # encode funcion python me lo 
#convierte en binario

hash_resultado = hashlib.sha256(contraseña_binaria).hexdigest()
#sha256 es un algoritmo que te permite crear el hash teniendo una entrada 
#si o si en numero binario
#hexdigest te permite se vuelva el objeto creado tipo hash un texto plano legible. nros y letras
#cierta longitud fijada.

print("El hash creado es: ", hash_resultado)
print("La contraseña que escribí fue: ", contraseña)

