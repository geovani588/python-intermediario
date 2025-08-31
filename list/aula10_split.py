"""
Split e join com list e str
split - divide uma string em lista
join - une uma string 
"""

frase = 'Olha so que,coisa interessante'
#lista_palavras = frase.split() # A função split() divide a string em uma lista de palavras
lista_palavras_cruas = frase.split(',')  # A função split() divide a string em uma lista de palavras usando a vírgula como delimitador

lista_palavras = []
for i, frase in enumerate(lista_palavras_cruas):
    lista_palavras.append(lista_palavras_cruas[i].strip())  # A função strip() remove espaços em branco no início e no final de cada palavra
    
    
#print(lista_palavras) # ['Olha so que', 'coisa interessante']
frase_unida = ', '.join(lista_palavras)  # A função join() une as palavras da lista em uma única string, separando-as por espaços
print(frase_unida)
