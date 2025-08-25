"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""
# Lembre-te de desempacotemanto

x, y, *resto = 1, 2, 3, 4
print(x, y, resto)  # x=1, y=2, resto=[3, 4]


#def soma(x, y):
#    return x + y

def soma(*args):
    total = 0
    for numero in args:
        print('total', total, numero)
        total += numero
        print('total final', total)
    print(total)

soma_1_2_3 = soma(1, 2, 3)
# print(soma_1_2_3)

soma_4_5_6 = soma(4, 5, 6)
# print(soma_4_5_6)

numeros = 1, 2, 3, 4, 5, 6, 7, 78, 10
outra_soma = soma(*numeros)
print(outra_soma)

print(sum(numeros))
# print(*numeros)


