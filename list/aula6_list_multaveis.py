"""
cuidados com dados mutáveis
= - copiado o valor (imutável)
= - aponta para o mesmo valor na memória (mutável) 
"""

lista_a = ['Luiz', 'Maria', 1, True, 1.2]
lista_b = lista_a.copy()  # aponta para o mesmo objeto na memória

lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)  # ['Qualquer coisa', 'Maria']