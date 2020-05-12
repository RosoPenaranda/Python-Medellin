
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matriz2 = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
           [[1, 2, 3], [4, 5, 6], [7, 8, 9]]]
for fila in matriz:
    print("\n fila: ", end="")
    for colum in fila:
        print(colum, end=" ")

print("")


print(matriz[2][2])

for fila in matriz2:
    for fila2 in fila:
        for ele in fila2:
            print(ele)
