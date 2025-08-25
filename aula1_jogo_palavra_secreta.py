"""
 faça um jogo para o usuario adivinhar qual
 a palavra secreta.
 - voce vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuario digitar apenas uma letra.
- Quando o suario digitar uma letra, voce
vai conferir se a letra digitada esta
na palavra secreta.
- Se a letra digitada estiver na
paravra secreta, exiba a letra;
 - Se a letra digitada não estiver
 na palavra secreta,exiba*.
 Faça a contagem de tentativas do seu usuário.
"""
# Jogo da Palavra Secreta


palavra_secreta = 'python'
letra_acertadas = ''
numero_tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1
    if len(letra_digitada) > 1:
        print('\nDigite apenas uma letra.')
        continue
    
    if letra_digitada in palavra_secreta:
        letra_acertadas += letra_digitada
    
    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letra_acertadas:
            palavra_formada += letra_secreta
        else:
           palavra_formada += '*'
    print('\nPalavra formada: ',palavra_formada)
    
    if palavra_formada == palavra_secreta:
        
        print('\nParabéns! Você acertou a palavra secreta.')
        print('\nA palavra secresta era: ', palavra_secreta)
        print('\nNúmero de tentativas:', numero_tentativas)
        
      
    
