# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)


from copy import deepcopy

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

novos_produtos = deepcopy(produtos)
for produto in novos_produtos:
    produto['preco'] *= 1.10  

produtos_ordenados_por_nome = deepcopy(produtos)
produtos_ordenados_por_nome.sort(key=lambda x: x['preco'], reverse=True)

produtos_ordenados_por_preco = deepcopy(produtos)
produtos_ordenados_por_preco.sort(key=lambda x: x['preco'])

print("Novos produtos com 10% de aumento:")
for produto in novos_produtos:
    print(f"{produto['nome']}: R$ {produto['preco']:.2f}")

print("\nProdutos ordenados por nome (decrescente):")
for produto in produtos_ordenados_por_nome:
    print(f"{produto['nome']}: R$ {produto['preco']:.2f}")

print("\nProdutos ordenados por preço (crescente):")
for produto in produtos_ordenados_por_preco:
    print(f"{produto['nome']}: R$ {produto['preco']:.2f}")