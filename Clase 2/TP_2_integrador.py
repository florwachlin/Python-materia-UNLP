#acceso y while true

#usuario = input("Ingrese su usuario: ")
contra= "1234"
contraseña = input("Ingrese su contraseña: ")

if contraseña == contra:

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

