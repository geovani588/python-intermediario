"""
Exercicio
Exiba os indices da lista
0 - Maria
1 - Helena
2 - Luiz 
"""

lista = ['Maria', 'Helena', "luiz"]
indices = range(len(lista))
for i in indices:
    print(f"{i} - {lista[i]}")

#for nome in lista:
    #print(nome, type(nome))