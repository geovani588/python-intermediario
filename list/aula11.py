"""
Lista de listas e seus indices 
"""

salas = [
    #0
    ['Maria', 'Helena', ], #0
    #0
    ['Eleine', ], #1
    #0        1     2
    ['Luiz', 'João', 'Eduardo', (0, 10, 20, 30, 40)], #2
]

print(salas[1] [0])
print(salas[0][1])
print(salas[2] [2])
print(salas[2] [3] [2])

for sala in salas:
    print(f'A sala e {sala}')
    for aluno in sala:
        print(aluno)