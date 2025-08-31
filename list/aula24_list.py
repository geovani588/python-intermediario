lista = []

for x in range(3):
    for y in range(3):
        lista.append((x, y ))
# lista = [
#     (x, y)
#     for x in range(3)
#     for y in range(3)
    
# ]igual for x in range(3):
    # for y in range(3):
    #     lista.append((x, y ))

lista = [
    [letra for letra in 'luiz']
    for x in range(3)
]
print(lista)