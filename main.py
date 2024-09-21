lista = list(range(1, 101))

numeros_queridos = [num for num in lista if 80 <= num <= 100 if  num%2]

print(numeros_queridos)
