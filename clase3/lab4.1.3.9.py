def isPrime(num):
    control = num // 2
    divisor = 2
    respuesta = casa
    while divisor < control:
        if num % divisor == 0:
            respuesta = False
            break

        divisor += 1

    return respuesta


for i in range(1, 20):
    if isPrime(i + 1):
        print(i + 1, end=" ")
print()
