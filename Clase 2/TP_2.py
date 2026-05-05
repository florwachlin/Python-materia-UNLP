#EJERCICIOS

#Ejercicio 6: Verificación de acceso con rol y contraseña

print("Seleccione su rol: ")
print("1. Administrador")
print("2. Moderador")
print("3. Usuario")

rol= input("Ingrese su rol: ")
rol= int(rol)

contraseña= input("Ingrese su contraseña: ")


if rol == 1 and contraseña == "1234":
    print("Bienvenido, Administrador")
    print("contraseña correcta")

    print("Elegi la opcion que desea realizar: ")
    print("1. Ver usuarios")
    print("2. Configuración")
    print("3. Salir")

    opcion =input("Ingrese su opción: ")
    opcion = int(opcion)

elif rol == 1 and contraseña != "1234":
    print("Usuario o contraseña inválidos")
elif rol != 1 and contraseña == "1234":
    print("Usuario válido, pero no es administrador")

    print("Seleccione la opción que desea realizar: ")
    print("1. Ver perfil")
    print("2. Cambiar contraseña")
    print("3. Salir")

elif rol != 1 or contraseña != "1234":
    print("Usuario o contraseña inválidos")