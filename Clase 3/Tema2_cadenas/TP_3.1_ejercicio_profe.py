#TP 3.1. EJERCICIO 1
#Uso de slicing y métodos de cadenas

#ejemplo alguien pone "1234-1234-1234-1234 "

tarjeta= input("Ingrese su numero de tarjeta (formato xxxx-xxxx-xxxx-xxxx): ")

#normalizo sin espacios ni guiones
tarjeta= tarjeta.strip() #le quito espacios en blanco inicio y final

if tarjeta.find("-") != 0 or tarjeta.find(" ") != 0:
    tarjeta = tarjeta.replace("-"," ")
    tarjeta = tarjeta.replace(" ","")
else:
    print("ningun remplazo es requerido")

print(f"Tarjeta normalizada {tarjeta}") #xxxxxxxxxxxxxxxx

#verifico son todos digitos, lo demas que no es espacio o -
pregunta= tarjeta.isdigit() #te dice true o false
opciones_maestro= ("50","56","57","58","6")

if pregunta == True and len(tarjeta) == 15 or len(tarjeta) == 16: #acepta el ingreso de dos tipos de programas 
    if tarjeta.startswith("4") == True:
        nombre_tarjeta = "Visa"
        print(f"Tarjeta {nombre_tarjeta} detectada")
        primeros_digitos= tarjeta[:5]
        print(f"Primeros 4 dígitos {primeros_digitos}")
        cantidad= len(tarjeta)
        print(f"Cantidad dígitos recibidos {cantidad}")

    elif tarjeta.startswith("5") == True:
        nombre_tarjeta = "Mastercard"
        print(f"Tarjeta {nombre_tarjeta} detectada")
        primeros_digitos= tarjeta[:5]
        print(f"Primeros 4 dígitos: {primeros_digitos}")
        cantidad= len(tarjeta)
        print(f"Cantidad dígitos recibidos {cantidad}")

    elif tarjeta.startswith("3") == True:
        nombre_tarjeta = "American Express / Diners"
        print(f"Tarjeta {nombre_tarjeta} detectada")
        primeros_digitos= tarjeta[:5]
        print(f"Primeros 4 dígitos: {primeros_digitos}")
        cantidad= len(tarjeta)
        print(f"Cantidad dígitos recibidos {cantidad}")


    elif tarjeta.startswith("62") == True:
        nombre_tarjeta = "Union Pay"
        print(f"Tarjeta {nombre_tarjeta} detectada")
        primeros_digitos= tarjeta[:5]
        print(f"Primeros 4 dígitos: {primeros_digitos}")
        cantidad= len(tarjeta)
        print(f"Cantidad dígitos recibidos {cantidad}")

    elif tarjeta.startswith("6") == True:
        nombre_tarjeta = "Discover"
        print(f"Tarjeta {nombre_tarjeta} detectada")
        primeros_digitos= tarjeta[:5]
        print(f"Primeros 4 dígitos: {primeros_digitos}")
        cantidad= len(tarjeta)
        print(f"Cantidad dígitos recibidos {cantidad}")

    elif tarjeta.startswith(opciones_maestro) == True: 
        nombre_tarjeta = "Maestro"
        print(f"Tarjeta {nombre_tarjeta} detectada")
        primeros_digitos= tarjeta[:5]
        print(f"Primeros 4 dígitos: {primeros_digitos}")
        cantidad= len(tarjeta)
        print(f"Cantidad dígitos recibidos {cantidad}")
    
    elif tarjeta.startswith("4") == True or tarjeta.startswith("5") == True :
        nombre_tarjeta = "Carte Bancaire"
        print(f"Tarjeta {nombre_tarjeta} detectada")
        primeros_digitos= tarjeta[:5]
        print(f"Primeros 4 dígitos: {primeros_digitos}")
        cantidad= len(tarjeta)
        print(f"Cantidad dígitos recibidos {cantidad}")

    else:
        print("Tipo detectado: Desconocida")
        primeros_digitos= tarjeta[:5]
        print(f"Primeros 4 dígitos: {primeros_digitos}")
        cantidad= len(tarjeta)
        print(f"Cantidad dígitos recibidos {cantidad}")