# Problema dos parametros mutaveis em funçoes Pyrhon

def adiciona_clientes(nome, lista = None): # coloca none
    if lista is None:
        lista = []
    lista.append(nome)
    return lista

lista1= []
cliente1 = adiciona_clientes('Luiz')
adiciona_clientes('Joana', cliente1)
adiciona_clientes('Matheus', cliente1)
adiciona_clientes('marta', cliente1)
cliente1.append('Edu') # igual mas curta


cliente2 = adiciona_clientes('Helena')
adiciona_clientes('Marcos', cliente2)

print(cliente1)
print(cliente2)