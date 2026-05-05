#Ejericios de slicing de cadena minis

palabra= "hola python"
print(palabra[-4])

#Ejercicio 1: 
# Objetivo: Obtener los últimos 4 dígitos de un número de tarjeta de crédito
# 1ero Pedir un número de tarjeta al usuario (Ejemplo: 1234-5678-9101-1121).

tarjeta = input("Ingrese digitos de tu targeta: ")
#extrayendo datos
ultimos_4_digitos = tarjeta[-4:]
print("Los ultimos digitos son: ", ultimos_4_digitos)
#o
print(f"Los ultimos dígitos son: {ultimos_4_digitos}")

#slicing 2.1
# Pedir un número de seguridad social ejemplo 123-45-6789

nss = input("Numero de seguridad social (formato: XXX-XX-XXXX): ")

# Validar si tiene 11 caracteres y el formato es correcto

if len(nss) == 11 and nss[3] == "-" and nss[6] == "-":
    print("Tiene el formato correcto")

else:
    print("Tiene el formato incorrecto")


#slicing 3
#Ejercicio 3: Extraer código de banco y número de cuenta
#Supongamos que los números de cuenta bancaria tienen el siguiente formato:
#XXXX-YYYY-ZZZZ, donde:

#XXXX: Código del banco.
#YYYY: Código de la sucursal.
#ZZZZ: Número de cuenta.

# Pedir el número de cuenta bancaria, ejemplos 1234-5678-8765
numero_cuenta_bancaria = input("Numero de cuenta bancaria: ")

# Extraer código de banco, sucursal y número de cuenta
codigo_banco = numero_cuenta_bancaria[0:4]
codigo_sucursal = numero_cuenta_bancaria [5:9]
codigo_numero_cuenta = numero_cuenta_bancaria [10:15]

print(f"Codigo del banco: {codigo_banco}")
print(f"Codigo sucursal: {codigo_sucursal}")
print(f"Codigo numero de cuenta:{codigo_numero_cuenta}")

#slicing 4: Verificar si un número es válido por su longitud
#Verificaremos si un número ingresado tiene la cantidad correcta de dígitos (por ejemplo, 16 para una tarjeta de crédito o 9 para un número de seguridad social).

# Pedir un número y su longitud esperada
tarjeta= input("Numero de tarjeta (formato xxxx xxxx xxxx xxxx): ")

# Verificar si la longitud es correcta
tarjeta = tarjeta.split() 
print(tarjeta)

if len(tarjeta) == 4:
    print("Longitud es correcta, comienza el programa")

else:
    print("Longitud incorrecta, siga el formato estipulado porfavor")