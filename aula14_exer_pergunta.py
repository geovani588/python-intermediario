# exercicio - sistema de perguntas e respostas

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

qtd_acertos = 0

for pergunta in perguntas:
    print('Pergunta' , pergunta['Pergunta'])
    print()
    
    for i, opcao in enumerate(pergunta['Opções']):
        print(f'{i})', opcao)
    print()
    
    escolha = int(input('Escolha uma opção: '))
    resposta_escolhida = pergunta['Opções'][escolha]
    
    if resposta_escolhida == pergunta['Resposta']:
        qtd_acertos += 1
        print('Acertou')
    else:
        print('Errou')
    print()
        
print('voce acertou' ,qtd_acertos )
print('de', len(perguntas), 'perguntas.')
