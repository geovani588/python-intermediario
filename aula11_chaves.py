#Manipulando chaves e valores em dicionario

pessoa = {}

chaves = 'nome'

pessoa[chaves] = 'Luiz Otavio'
pessoa['sobrenome'] = 'miranda'


print(pessoa[chaves]) # Luiz Otavio

print(pessoa) # vai da chave completa {'nome': 'Luiz Otavio'}

pessoa[chaves] = 'Maria'

del pessoa['sobrenome']
print(pessoa)
print(pessoa['nome'])

# print(pessoa.get('sobrenome'))
if pessoa.get('sobrenome') is None:
    print('NÃO EXISTE')
else:
    print(pessoa['sobrenome'])

# print('ISSO Não vai')