import json

pessoa = {
    'nome': 'Luiz Otavio 2',
    'sobrenome': 'Miranda',
    'enderecos': [
        {'rua': 'R1', 'numero': 32},
        {'rua': 'R2', 'numero': 55},
    ],
    'altura': 1.8,
    'numeros_preferidos': (2, 4, 6, 8, 10),
    'dev': True,
    'nada': None,
}

with open('aula1_json.json','w', encoding='utf8') as arquivo: #  encoding='utf8' para tira problema de acentos
    json.dump(pessoa, 
              arquivo, 
              ensure_ascii=False, 
              indent=2)
    
with open('aula1_json.json', 'r', encoding='utf8') as arquivo:
    pessoa = json.load(arquivo)
    print(pessoa)
    print(type(pessoa))
    print(pessoa['nome'])