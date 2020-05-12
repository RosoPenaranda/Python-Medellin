import os


def limpiarPantalla():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def formatearDatos(datos):
    valores = datos.split(',')
    return (int(valores[0]), int(valores[1]))


def cargarDatos(fileName):
    file = open(fileName)

    contenido = file.read().split('\n')

    datos = list(map(formatearDatos, contenido[1:]))
    cabecera = contenido[0].split(',')
    return {"header": cabecera, "datos": datos}


def promedio(datos):
    cantidad = len(datos)
    suma = 0
    for x in datos:
        suma += x[0]

    return suma/cantidad


def promedioPonderado(datos):
    creditos = 0
    acumulado = 0

    for dato in datos:
        creditos += dato[1]
        acumulado += dato[0]*dato[1]

    return acumulado/creditos


def mediana(datos):
    mediana = 0
    if len(datos) % 2 == 0:
        aux = int(len(datos)/2)
        mediana = ((datos[aux][0] + datos[aux-1][0])/2)
    else:
        mediana = datos[int(len(datos)/2)][0]

    return mediana


def moda(datos):
    contadores = set()
    for nota in datos:
        cont = 0
        for dato in datos:
            if dato[0] == nota[0]:
                cont += 1

        contadores.add((nota[0], cont))

    mayor = 0
    moda = 0
    for elem in contadores:
        if elem[1] > mayor:
            mayor = elem[1]
            moda = elem[0]
    print(contadores)
    return moda


# datos = cargarDatos('creditos.csv')
# print(promedio(datos['datos']))

def main():
    fileName = None

    if fileName == None:
        fileName = input('Ingrese el nombre del archivo: ')

    datos = cargarDatos(fileName)
    salir = False

    while(not(salir)):
        print('''
          Elija el número de la operacion a realizar:
          1 - Calcular promedio.
          2 - Calcular promedio Ponderado
          3 - Ordenar los datos.
          4 - Calcular Mediana
          5 - Moda
          6 - Quartiles
          0 - Finalizar \n
          ''')

        operacion = input('Operacion: ')

        if operacion == '1':
            limpiarPantalla()
            print("Promedio: ", promedio(datos['datos']))

        if operacion == '2':
            limpiarPantalla()
            print("Promedio Ponderado: ", promedioPonderado(datos['datos']))

        if operacion == '3':
            limpiarPantalla()
            datos['datos'].sort(key=lambda elem: elem[0])
            print("Los datos fueron ordenados: ", datos["datos"])

        if operacion == '4':
            limpiarPantalla()
            print('Mediana: ', mediana(datos['datos']))

        if operacion == '5':
            limpiarPantalla()
            print("Moda: ", moda(datos['datos']))

        if operacion == '6':
            limpiarPantalla()
            temp = datos['datos']
            datosQua1 = temp[0:int(len(temp)/2)]
            datosQua3 = temp[int((len(temp)+1)/2):]

            print("Q1: ", mediana(datosQua1))
            print("Q2: ", mediana(temp))
            print("Q2: ", mediana(datosQua3))

        if operacion == '0':
            salir = True

    print("Adios")


if __name__ == '__main__':
    main()
