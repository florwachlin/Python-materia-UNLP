#TP LISTAS
# Práctica: Manejo de Listas Anidadas en Python.
# Objetivo: Aprender a trabajar con listas anidadas en Python, almacenar información y realizar cálculos.

alumnos = []

while True: #mientras condicion de arriba sea verdadera haces todo lo que sigue

#le pregunto usuario que quiere hacer
    pregunta = input("Querés agregar un nuevo alumno, a la lista (si/no)?").lower().strip()
    #strip elimina espacios inicio y final 

    if pregunta == "si":   
        nombre_alumno = input("Ingrese nombre del alumno: ")
        nota_1= float(input("Ingrese primer nota del alumno: "))
        nota_2= float(input("Ingrese segunda nota del alumno: "))
        nota_3= float(input("Ingrese tercera nota del alumno: "))
        notas=[nota_1, nota_2, nota_3]

        promedio_notas= (sum(notas)) / 3

        lista_alumno = [nombre_alumno, nota_1, nota_2 , nota_3 , promedio_notas]
    
        alumnos.append(lista_alumno)

        #imprimo lista de alumnos de la fila que el usuario esta rellenando
        print("\nLista de alumnos:")
        for alumno in alumnos:
            print(f"Nombre: {alumno[0]}, Notas: {alumno[1:4]}, Promedio: {alumno[4]}")

        continue #te vuelve a preguntar

    elif pregunta == "no":
        print("Rechazada la opcion agregar alumno\nNos vemos la proxima")
        break

    else:
        print("Respuesta no valida, sigue el formato porfavor")
     



