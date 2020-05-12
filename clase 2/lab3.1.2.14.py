'''
el ejercicio tiene las siguientes condiciones:

- La piramide se comienza a construir desde la punta.
- Cada piso tiene 1 bloque mas que el piso anterior.
- Si no se puede completar un piso con la condición anterior se descarta
  ese ultimo piso, y lo bloques sobrantes. 
  Ejemplo con 5 bloques:
  piso 1:    |
  piso 2:   | |
  piso 3:  | | 
  el ultimo piso no se puede completar por lo cual la altura de la piramide
  que se puede construir con 5 bloques es 2.
'''


bloques = int(input("Ingrese el número de bloques: "))

# Colocamos la altura inicial en 0, esto nos ayudara también con el numero de
# bloques necesarios por piso.
altura = 0

# mientras el numero de bloques sea superior a la altura, garantizamos que se puede
# construir un piso, el piso 1 necesita 1 bloque, el 2 necesita 2 bloques y así
# los siguientes pisos.
while bloques > altura:
    # la siguiente linea asume la creación de un piso de la piramide
    bloques = bloques - altura

    # en este condicional comenzamos a modificar la condición de parada
    # se garantiza la misma para todo número positivo aun no estamos viendo
    # manejo de excepciones por lo cual se asume que el usuario siempre ingresa
    # un número positivo
    if bloques > altura:
        altura = altura + 1


print("La altura de la pirámide:", altura)



bloques = int(input("Ingrese el número de bloques: "))

altura = 0

while bloques > altura:
    bloques = bloques - altura

    if bloques > altura:
        altura = altura + 1

print("La altura de la pirámide:", altura)