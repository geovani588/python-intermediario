# Exercicios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

numero = int(input('Digite um número duplicar: '))
numero1 = int(input('Digite um número triplicar: '))
numero2 = int(input('Digite um número quadruplicar: '))

def duplicar(numero):
    return numero * 2

def triplicar(numero1):
    return numero1 * 3

def quadruplicar(numero2):
    return numero2 * 4


print(f'Duplicado: {duplicar(numero)}')
print(f'Duplicado: {triplicar(numero1)}')
print(f'Duplicado: {quadruplicar(numero2)}')

