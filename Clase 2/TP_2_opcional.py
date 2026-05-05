while True: #bucle infinito
    print("Seleccione la opcion que desea: ")
    print("1. Ver telefonos móviles ")
    print("2: Ver laptops: ")
    print("3: Ver televisores: ")
    print("4: Ver auticulares: ")
    print("5. Salir del sistema: ")

    opcion= input("Ingrese su opcion: ")
    opcion = int(opcion)

    if opcion == 1:
        print("Telefonos móviles opciones: ")
        print("Iphone 14: 899 dolares")
        print("Samsumg Galaxy S22: 799 dolares")

        print("Seleccione la opcion que desea: ")
        print("1. Volver al menu principal")
        print("2. Salir del sistema")
        opcion2 = input("Ingrese su opcion: ")
        opcion2 = int(opcion2)
        if opcion2 == 1:
            print("Volviendo al menu principal...")
            continue

        elif opcion2 == 2:
            print("Saliste del programa, nos vemos")
            break

        else: 
            print("Opcion no es correcta, volviendo al menu principal...")
            continue    

    elif opcion == 2: 
        print("Laptops opciones: ")
        print("Macbook Air: 999 dolares")
        print("Dell XPS 13: 899 dolares")

        print("Seleccione la opcion que desea: ")
        print("1. Volver al menu principal")
        print("2. Salir del sistema")
        opcion2 = input("Ingrese su opcion: ")
        opcion2 = int(opcion2)
        if opcion2 == 1:
            print("Volviendo al menu principal...")
            continue

        elif opcion2 == 2:
            print("Saliste del programa, nos vemos")
            break

        else: 
            print("Opcion no es correcta, volviendo al menu principal...")
            continue

    elif opcion == 3: 
        print("Televisores opciones: ")
        print("Samsung 55 4K 650 dolares")
        print("LG65 OLED: 1200 dolares")

        print("Seleccione la opcion que desea: ")
        print("1. Volver al menu principal")
        print("2. Salir del sistema")
        opcion2 = input("Ingrese su opcion: ")
        opcion2 = int(opcion2)
        if opcion2 == 1:
            print("Volviendo al menu principal...")
            continue

        elif opcion2 == 2:
            print("Saliste del programa, nos vemos")
            break

        else: 
            print("Opcion no es correcta, volviendo al menu principal...")
            continue
                
            
    elif opcion == 3: 
        print("Televisores opciones: ")
        print("Samsung 55 4K 650 dolares")
        print("LG65 OLED: 1200 dolares")

        print("Seleccione la opcion que desea: ")
        print("1. Volver al menu principal")
        print("2. Salir del sistema")
        opcion2 = input("Ingrese su opcion: ")
        opcion2 = int(opcion2)
        if opcion2 == 1:
            print("Volviendo al menu principal...")
            continue

        elif opcion2 == 2:
            print("Saliste del programa, nos vemos")
            break

        else: 
            print("Opcion no es correcta, volviendo al menu principal...")
            continue

    elif opcion == 4: 
        print("Auriculares opciones: ")
        print("Sony WH-1000XM4: 350 dolares")
        print("Bose QuietComfort 35 II: 299 dolares")

        print("Seleccione la opcion que desea: ")
        print("1. Volver al menu principal")
        print("2. Salir del sistema")
        opcion2 = input("Ingrese su opcion: ")
        opcion2 = int(opcion2)
        if opcion2 == 1:
            print("Volviendo al menu principal...")
            continue

        elif opcion2 == 2:
            print("Saliste del programa, nos vemos")
            break

        else: 
            print("Opcion no es correcta, volviendo al menu principal...")
            continue

            
    elif opcion == 5: 
        print("Saliste del sistema, nos vemos")

        print("Seleccione la opcion que desea: ")
        print("1. Volver al menu principal")
        print("2. Salir del sistema")
        opcion2 = input("Ingrese su opcion: ")
        opcion2 = int(opcion2)
        if opcion2 == 1:
            print("Volviendo al menu principal...")
            continue

        elif opcion2 == 2:
            print("Saliste del programa, nos vemos")
            break

        else: 
                print("Opcion no es correcta, volviendo al menu principal...")

    else: 
        print("Opción es invalida")

