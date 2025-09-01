# combinations, Permutations e Products - Itertools
# Combinação = Ordem não importa - Iteravel + tamanho do grupo
# Permutação = Ordem importa
# Produto = Ordem importa e repete valores unicos

from itertools import combinations, permutations, product

def print_iter(iterator):
    print(*list(iterator), sep='\n')
pessoas = [
    'joao', 'Joana', 'Luiz', 'leticia'
]
camisetas = [
    ['preta', 'branca'],
    ['p', 'm','g'],
    ['masculino', 'feminino']
]

print("Combinations (pessoas, 2):")
print_iter(combinations(pessoas, 2))

print("\nPermutations (pessoas, 2):")
print_iter(permutations(pessoas, 2))

print("\nProduct (pessoas x camisetas):")
print_iter(product(pessoas, *camisetas))