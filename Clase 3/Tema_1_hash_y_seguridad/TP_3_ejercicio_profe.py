# 1 ero calculo el hash de la contraseña que es flor

import hashlib
import getpass

usuario = "admin"

#contraseña = "flor"

#contraseña_binaria = contraseña.encode() #si o si debe la contra ser string
#hash_resultado = hashlib.sha256(contraseña_binaria).hexdigest()
#print(hash_resultado)

hash_contraseña = "1aedac41cf160ca5b45faf3e3ff702a84482db37416af707ac055fef2584cdd9"

#---usuario---#


max_intentos = 3
intentos = 0

while intentos < max_intentos:
    
    usuario_entrada = input("Ingrese su usuario: ")
    contraseña_entrada = getpass.getpass("Ingrese su contraseña: ")

    contraseña_entrada_binaria = contraseña_entrada.encode()
    hash_entrada = hashlib.sha256(contraseña_entrada_binaria).hexdigest()

    if usuario_entrada == usuario and hash_entrada == hash_contraseña:
    
        while True: #lopee infinitamente esto
            import math

            print("Bienvenido, usted ha accedido al menu de funciones de la libreria math")
            print("1: Raiz cuadrada")
            print("2: Potencia")
            print("3: Seno")
            print("4: Salir del programa")
            opcion = input("Eliga la opción (1-4): ")

            if opcion == "1":
                raiz= input("Numero le queres calcular la raiz cuadrada: ")
                raiz= int(raiz)
                raiz= math.sqrt(raiz)
                print("La raiz cuadrada es: ", raiz)

            elif opcion == "2":
                a= input("Ingrese la base de la potencia: ") 
                b= input("Ingrese el exponente: ")
                a=int(a)
                b=int(b)
                resultado= math.pow(a,b)
                print("El resultado es: ", resultado)

            elif opcion == "3":
                angulo_radian= input("Ingrese angulo en radianes: ")
                angulo_radian = float(angulo_radian)
                resultado= math.sin(angulo_radian)
                print("Angulo en radianes: ", resultado)

            elif opcion == "4":
                print("Saliendo, nos vemos la próxima!")
                break #rompe el bucle while true infinito 
            
            else:
                print("Opcion incorrecta, intente nuevamente")
                continue #interrumpe seguir por esta linea
                        #y vuelve a empezar el bucle

    else: 
        print("Usuario o contraseña incorrecta")
        intentos += 1

print("Bloqueado, superaste el límite de intentos posibles")
