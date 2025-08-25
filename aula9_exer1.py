"""
Faça uma lista de comprar com listas 
O usuario deve ter a possibidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de indices inexistentes na lista
"""


lista = []

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        valor = input('Valor: ')
        lista.append(valor)

    elif opcao == 'a':
        indice_str = input('Escolha o índice para apagar: ')
        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor, digite um número inteiro.')
       
    elif opcao == 'l':

        if not lista:
            print('Nada para listar')
        else:
            for i, valor in enumerate(lista):
                print(i, valor)

    else:
        print('Por favor, escolha i, a ou l.')
