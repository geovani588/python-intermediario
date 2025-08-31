"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD) 
"""



lista = [10, 20, 30, 40]
lista.append('Luiz')
nome = lista.pop()
lista.append('Maria')
del lista[0]
#lista.clear() # limpa a lista
lista.insert(0, 5) # insere o valor 5 no índice 0
print(lista)
print(lista[2]) # Acessa o elemento no índice 2