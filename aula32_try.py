#Try, except, else e finally 

try:
    numero1 = int(input("Digite um número inteiro: "))
    numero2 = int(input("Digite um número inteiro: "))
    soma = numero1 + numero2
    subtracao = numero1 - numero2
    multiplicacao = numero1 * numero2
    media = (numero1 + numero2) / 2
    print(f"Você digitou os números {numero1} e {numero2}")
    print(f"Soma: {soma}")
    print(f"Subtração: {subtracao}")
    print(f"Multiplicação: {multiplicacao}")
    print(f"Média: {media}")
except ValueError:
    print("Erro: você não digitou um número inteiro válido.")

print("Fim do programa, continuar executando...")