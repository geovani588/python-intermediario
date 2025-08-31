"""lista = [10, 20, 30, 40]
numero = lista [2]
print(numero)"""


#--------0---1---2----3--4---5
lista = [10, 20, 30, 40, 50, 60]
lista [2] = 300
del lista [2] # remove o elemento no indice 2
lista.append(70) # adiciona o elemento 70 no final da lista
lista.pop() # remove o ultimo elemento da lista
lista.append(80) # adiciona o elemento 80 no final da lista
ultimo_valor = lista.pop() # remove o ultimo elemento da lista e armazena na variavel
print(lista, 'removido:', ultimo_valor)

print(lista)
print(lista[2])

