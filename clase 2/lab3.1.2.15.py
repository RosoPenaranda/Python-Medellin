c0 = int(input("Ingresa un número mayor que 0: "))

if c0 <= 0:
    print("El número debe ser mayor que 0")
pasos = 0

while True:

    if c0 % 2 == 0:
        c0 = c0 / 2
    else:
        c0 = 3*c0 + 1

    pasos += 1
    print(c0)

    if c0 == 1:
        break

print("pasos: ", pasos)
