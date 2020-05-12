numeroSecreto = 777

print(
    """
    +==================================+
    | Bienvenido a mi juego, muggle!   |
    | Introduce un número entero       |
    | y adivina qué número he          |
    | elegido para ti.                 |
    | Entonces,                        |
    | ¿Cuál es el número secreto?      |
    +==================================+
    """)

while True:

    n = int(input())
    if n != numeroSecreto:
        print("¡Ja, ja! ¡Estás atrapado en mi ciclo!")
    else:
        break


print("¡Bien hecho, muggle! Eres libre ahora")
