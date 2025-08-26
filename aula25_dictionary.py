# Dictionary Comprehension e set comprehension

produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritorio',
}

dc = {
    chave: valor.upper()# string tem q usar if para funcionar
    if isinstance(valor, str)else valor
    for chave, valor
    in produto.items()
    if chave!= 'categoria' # que for diferente categoria vai tirar categoria
}
print(produto)


lista = [
    ('a', 'valor a'),
    ('b', 'valor b'),
    ('c', 'valor c')
]

dc = {
    chave: valor 
    for chave,valor in lista 
}

#s1 = {i for i in range (10)}
print(set(range(10)))
print(lista)