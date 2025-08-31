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
#concatena listas
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b  # Concatena as listas
lista_d = lista_a.extend(lista_b)  # Extende a lista_a com os elementos de lista_b  
print(lista_c)  # Exibe a lista concatenada
print(lista_a)  # Exibe a lista estendida ele mexe na lista_a