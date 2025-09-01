from functools import partial

def print_iter(iterable):
    for item in iterable:
        if isinstance(item, dict) and 'preco' in item:
            print(f"{item['nome']}: R$ {item['preco']:.2f}")
        else:
            print(item)
    print('')

# Função base
def multiplica(x, const):
    return x * const

# Cria versão dobrada
dobra = partial(multiplica, const=2)
print("Dobro de 50:", dobra(50))

# Função base para aumento percentual
def aumenta_percentual(valor, percentual):
    return valor * (1 + percentual / 100)

# Cria versão com aumento fixo de 20%
aumenta20 = partial(aumenta_percentual, percentual=20)
print("10 aumentado em 20%:", aumenta20(10))

# Lista de produtos
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

print('Preço antigo dos produtos:')
print_iter(produtos)

# Cria nova lista com os preços aumentados
novos_produtos = list(
    map(lambda d: {**d, 'preco': aumenta20(d['preco'])}, produtos)
)

print('Aumento de preço nos produtos:')
print_iter(novos_produtos)
