# map, partial, GeneratorType e esgotamento de Iterators

from functools import partial
from types import GeneratorType


# map - para mapear dados
def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

def aumentar_procentagem(valor, porcentagem):
    return round(valor * porcentagem, 2)

aumentar_dez_porcento = partial(
    aumentar_procentagem,
    porcentagem = 1.1
)

# novos_produtos = [
#     {**p,
#         'preco': aumentar_dez_porcento(p['preco'])}
#     for p in produtos
# ]

def muda_preco_de_produtos(produto):
    return {
        **produto,
        'preco': aumentar_dez_porcento(
            produto['preco']
        )
    }


novos_produtos = list(map(
    muda_preco_de_produtos,
    produtos
))


print_iter(produtos)
print()
print('10%')
print_iter(novos_produtos)

print(
    list(map(
        lambda x: x * 3,
        [1, 2, 3, 4]
    ))
)


from functools import partial
from types import GeneratorType

def executa(func, *args, **kwargs):
return func(*args, **kwargs)

def multiplica(num, const):
return num * const

def print_iter(iterable):
print(*iterable, sep='\n')
print('')

dobra = partial(multiplica, const=2)

print(dobra(50))

percentaumentvin = partial(lambda x, y: x*(1+ (y/100)), y=20)

print(percentaumentvin(10))

produtos = [
{'nome': 'Produto 5', 'preco': 10.00},
{'nome': 'Produto 1', 'preco': 22.32},
{'nome': 'Produto 3', 'preco': 10.11},
{'nome': 'Produto 2', 'preco': 105.87},
{'nome': 'Produto 4', 'preco': 69.90},
]

print('Preço antigo dos produtos: ')
print_iter(produtos)

novosprodutos = list(map(lambda dicionario: {**dicionario, 'preco': percentaumentvin(dicionario['preco'])}, produtos))

print('')
print('Aumento de preço nos produtos: ')
print_iter(novosprodutos)

