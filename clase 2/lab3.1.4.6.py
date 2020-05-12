# Esta es una lista existente de números ocultos en el sombrero.
listaSombrero = [1, 2, 3, 4, 5]

# Paso 1: escribe una línea de código que solicite al usuario
n = int(input("ingrese posición a reemplazar: "))

# para reemplazar el número de en medio con un número entero ingresado por el usuario.

listaSombrero[2] = n

# Paso 2: escribe aquí una línea de código que elimine el último elemento de la lista.
listaSombrero.pop()
# Paso 3: escribe aquí una línea de código que imprima la longitud de la lista existente.
print('tamaño: ', len(listaSombrero))
print(listaSombrero)
