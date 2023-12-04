filename = "input.txt"
soma = 0
numero = ''

with open(filename) as f:
    for line in f:
        numero = ''.join(char for char in line if char.isdigit())
        numero = str(numero[0]) + str(numero[-1])
        soma += int(numero)

print(soma)