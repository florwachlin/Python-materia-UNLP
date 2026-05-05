import hashlib
import getpass

usuario = "admin"
contraseña_hasheada = "11a4a60b518bf24989d481468076e5d5982884626aed9faeb35b8576fcd223e1"
#probe con "python"

#para obtener el hash hago aparte esto :
#contra_binaria= contra.encode()
#hash_resultado= hashlib.sha256(contra_binaria).hexdigest()
#print(hash_resultado)

#--- Inicio de sesión usuario --- #

usuario_entrada = input("Ingrese su usuario: ")
contra_entrada = getpass.getpass("Ingrese su contraseña: ")
#el getpass actuar como un input pero no muestra que valor completa la persona por seguridad

contra_binaria= contra_entrada.encode()
hash_resultado= hashlib.sha256(contra_binaria).hexdigest()

if usuario == usuario_entrada and hash_resultado == contraseña_hasheada:

    while True: #mientras esto sea de verdad la condicion previa
        print("Bienvenido, usuario")
        print("Seleccione la opcion que desea realizar: ")
        print("1. Suma")
        print("2.Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")

        opcion= input("Ingrese su opción: ")
        opcion= int(opcion)

        if opcion == 1 or opcion == 2 or opcion == 3 or opcion == 4:        
            a= int(input("Ingrese el primer numero: "))
            b= int(input("Ingrese el segundo numero: "))

            if opcion == 1:
                resultado = a + b
                print("El resultado de la suma es: ", resultado)
            elif opcion == 2:
                resultado = a - b
                print("El resultado de la resta es: ", resultado)
            elif opcion == 3:
                resultado = a * b
                print("El resultado de la multiplicación es: ", resultado)
            elif opcion == 4:
                resultado = a / b
                print("El resultado de la división es: ", resultado)
            elif opcion == 5:
                print("Saliste del programa, nos vemos")
                break
            else:
                print("Opcion no valida")
        
else:
    print("Error: Contraseña incorrecta")

