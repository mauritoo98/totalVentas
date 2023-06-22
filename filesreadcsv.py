datos=open("datos.csv", "r")
_=datos.readline()

def menu ():
    opcion= int(input("Ingrese 1 para venta por trimestres, 2 para ventas por año y 3 promedio por año, 0 para salir"))

    if opcion==1:
        ventaTrimestre()
    elif opcion==2:
        ventaAnual()
    elif opcion==3:
        promedioAnual()
    elif opcion==0:
        quit
    else:
        print("Ingrese una opicion correcta")
        menu()


def ventaTrimestre():
    totalTrimestre = 0
    opcionTrimestre = int(input("Ingrese el trimestre que quiere saber(de 1 al 4)"))
    for linea in datos.readlines():
        datos_separados = linea.split(";")
        dat= int(datos_separados[opcionTrimestre])
        totalTrimestre=totalTrimestre+dat
    print("El total del ", opcionTrimestre, " es ", totalTrimestre)
    datos.close()

def ventaAnual():
    año = int(input("Ingrese el año a buscar: "))
    totalAnual = 0
    acum=0
    for linea in datos.readlines():
        datos_separados = linea.strip().split(";")
        if int(datos_separados[0]) == año:
            while acum<4:
                acum = acum+1
                precio = int(datos_separados[acum])
                totalAnual=precio+totalAnual
    if totalAnual>0:
        print("El total del año: ",año, " es ", totalAnual)
    else:
        print("Ese año no existe")
    datos.close()

def promedioAnual():
    año = int(input("Ingrese el año a buscar: "))
    totalAnual = 0
    acum = 0
    for linea in datos.readlines():
        datos_separados = linea.strip().split(";")
        if int(datos_separados[0])== año:
            while acum<4:
                acum= acum+ 1
                precio=int(datos_separados[acum])
                totalAnual=totalAnual+precio
    if totalAnual>0:
        totalAnual= totalAnual//12
        print("El promedio del año: ",año, " es ", totalAnual)
    else:
        print("Ese año no existe") 


menu()
