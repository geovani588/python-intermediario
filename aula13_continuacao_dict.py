# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - A paga o último item adicionado
# update - Atualiza um dicionário com outro

p1 = {
    'nome': 'Luiz',
    'sobrenome': 'Miranda',
}

#print(p1['nome'])
#print(p1.get('nome', 'Nao existe'))

#nome = p1.pop('nome')
#print (nome)
#print (p1)


#ultima_chave = p1.popitem()
#print (ultima_chave)
#print (p1)
#p1.update({ # atulizar valores
#    'nome': 'novo valor',
#    'idade': 30
#})
#p1.update(nome='novo valor', idade = 30) # outra forma
tupla = ('nome', 'novo valor'), ('idade', 30) # outra forma
p1.update(tupla)
print(p1)