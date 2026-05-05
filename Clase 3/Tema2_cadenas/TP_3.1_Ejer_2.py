#EJERCICIO 2 CADENAS. validar formato de CBU

#ejemplo 011-0001-2-1234567890123-5

cbu= input("Ingrese su número de CBU (formato: xxx-xxxx-x-xxxxxxxxxxxxx-x) ")

#normalizo 
#le quito espacios inicio y final, reemplazo - por espacios, elimino espacios

cbu = cbu.strip()

if cbu.find("-") or cbu.find(" "):
    cbu= cbu.replace("-"," ")
    cbu= cbu.replace(" ","")
    print(cbu)
    
else:
    print("Listo reemplazos")

#hasta ahora tengo algo así xxxxxxxxxxxxxxxxxxx
#debo verificar son numeros, y tienen la longitud deseada

#verifico tema longitud + slicing + tipo de banco
if len(cbu) == 22: #cantidad letras
    print(f"Número normalizado:{cbu}")
    print("El formato es el correcto")

    #slicing extraigo datos
    codigo_banco= cbu[0:4] #o [:3]
    numero_de_sucursal_1= cbu[3:7]
    digito_de_control= cbu[7]
    numero_de_cuenta= cbu[9:23]
    digito_de_control_2= cbu[-1]

    #diccionario/glosario de codificación
        #007	BANCO DE GALICIA Y BUENOS AIRES S.A.
        #011	BANCO DE LA NACION ARGENTINA
        #014	BANCO DE LA PROVINCIA DE BUENOS AIRES

    if codigo_banco == "007":
        nombre_banco= "BANCO DE GALICIA Y BUENOS AIRES S.A."
    elif codigo_banco == "011":
        nombre_banco = "BANCO DE LA NACION ARGENTINA"
    elif codigo_banco == "014":
        nombre_banco = "BANCO DE LA PROVINCIA DE BUENOS AIRES"
    else:
        nombre_banco = "Desconocido"

    print(f"Número de cuenta {numero_de_cuenta}\nPertenece al banco {nombre_banco}\nCuya sucursal es {numero_de_sucursal_1}")

else:
    print("Cantidad de digitos escritos incorrecto")