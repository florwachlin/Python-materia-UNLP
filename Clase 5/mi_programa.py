import hashlib
import getpass
import math

#contra_entrada= getpass.getpass("Ingrese su contraseña")
#contra_binaria = contra_entrada.encode() 
#contra_hasheada= hashlib.sha256(contra_binaria).hexdigest()
#print(contra_hasheada)

usuario= "admin"
contra_hash= "a8a15faedf1420db2b80e81fe86167d785aaafb2c4da29bc55637ac1de7751d9"

#---- funciones propias

def generar_hash_usuario(contra):
    return hashlib.sha256(contra.encode()).hexdigest()
    #la salida es una contraseña hasheada, del usuario


def menu():
    print("Elije una opcion: ")
    print("1: Convierte grados a radianes")
    print("2: Convierte radianes a grados")
    print("3: Calcula el seno de un angulo (radianes)")
    print("4: Calcula el coseno de un angulo (radianes)")
    print("5: Salir")


def grados_a_rad():
    angulo= input("Angulo de entrada en grados (Formato (x.y): ")
    if "," in angulo:
        angulo= angulo.replace(",",".")
        
    try: #todavia nose si es una string por ende pruebo pasarlo a float
        angulo = float(angulo)
        angulo_radianes = math.radians(angulo)
        
    except: #si es una string, va a esta linea
        print("Formato incorrecto")
        return None #porque si viene a esta linea no existe ninguna variable de salida

    return angulo_radianes


def rad_a_grados():
    angulo_rad = input("Angulo de entrada en radianes (En formato (x.y)): ")
    if "," in angulo_rad: #solo cambio coma con puntos
        angulo_rad = angulo_rad.replace(",",".")
    
    #si tiene palabra . palabra ... cuando pruebe pasarlo a float, no te dejaria
    try:
        angulo_rad = float(angulo_rad)
        angulo_grados = math.degrees(angulo_rad)
        print(angulo_grados)
    except:
        print("Formato incorrecto")
        return None

    return angulo_grados

def sen_rad():
    angulo_rad = input("Angulo de entrada en radianes (En formato (x.y)): ")
    if "," in angulo_rad: #solo cambio coma con puntos
        angulo_rad= angulo_rad.replace(",",".")
    
    #si tiene palabra . palabra ... cuando pruebe pasarlo a float, no te dejaria
    try:
        angulo_rad = float(angulo_rad)
        seno_angulo = math.sin(angulo_rad)
        print(seno_angulo)
    except:
        print("Formato incorrecto")
        return None 
    
    return(seno_angulo) 

def cos_rad():
    angulo_rad= input("Angulo de entrada en radianes (En formato (x.y)): ")
   
    if "," in angulo_rad: #solo cambio coma con puntos
        angulo_rad= angulo_rad.replace(",",".")
    
    #si tiene palabra . palabra ... cuando pruebe pasarlo a float, no te dejaria
    try:
        angulo_rad = float(angulo_rad)
        cos_angulo = math.cos(angulo_rad)
        print(cos_angulo)
    except:
        print("Formato incorrecto")
        return None

    return(cos_angulo) 

#---- main 

contador=0
while contador <3:

    usuario_entrada= input("Ingrese su nombre de usuario: ")
    #hashear lo que entre de contra
    contra_usuario= getpass.getpass("Ingrese su contraseña: ")
    contra_hash_usuario = generar_hash_usuario(contra_usuario)


    if usuario == usuario_entrada and contra_hash == contra_hash_usuario:
            
        while True: #bucle infinito, todo lo que este dentro seguira, salvo exista un break

            menu()
            opcion= input("Opcion deseada: ")

            if opcion == "1":
                angulo_radianes_ext = grados_a_rad() #llama a la función y atrapa su salida a esta variable
                #con print en la funcion, la salida de consola no me permitiria guardarla en una variable, la llamada de la función
                print(f"Angulo en grados transformado a radianes: {angulo_radianes_ext}")
                
            elif opcion == "2":
                rad_a_grados_ext= rad_a_grados()
                print(f"Angulo en radianes transformado a grados: {rad_a_grados_ext}")

            elif opcion == "3":
                sen_rad_ext= sen_rad()
                print(f"El seno del angulo ingresado es {sen_rad_ext}")
                
            elif opcion == "4":
                cos_rad_ext= cos_rad()
                print(f"El coseno del angulo ingresado es {cos_rad_ext}")
                
            elif opcion == "5":
                print("Saliendo del programa, gracias por elejirnos")
                break #salgo del while true

            else:
                print("Opcion invalida, seleccione una opcion correcta")

    else:
        print("Usuario o contraseña invalida")
        contador+= 1


if contador == 3:
    print("Maxima cantidad de intentos probados, vuelva mas tarde")


                
                
