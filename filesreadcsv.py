datos=open("datos.csv", "r")
_=datos.readline()

def menu ():
    opcion= int(input("Ingrese 1 para venta por trimestres, 2 para ventas por año y 3 promedio por año"))

    if opcion==1:
        ventaTrimestre()
    elif opcion==2:
        ventaAnual()


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
    print("El total del año: ",año, " es ", totalAnual)
    datos.close()


menu()
