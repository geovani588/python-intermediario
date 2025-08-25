# Exercicios com funcoes

#crie uma funcao que multiplica todos os argumentos
#nao nomeados recebidos
#retorne o total para uma variavel e mostre o valor
# da variavel

# crie uma funcao fala se um numero e par ou impar
# retorne se o numero e par ou impar

def multiplica(*args):
    total = 2
    for numero in args:
        total *= numero
    return total

print(multiplica(1, 2,3))
print(multiplica(4, 5))

def par_ou_impar(numero):
    if numero % 2 == 0:
        return 'par'
    else:
        return 'impar'
print(par_ou_impar(7))
print(par_ou_impar(8))  