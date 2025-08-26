# ISINSTACE - PARA SABER SE OBJETO E DE DETERMINADO TIPO

lista = [ 
        'a', 1, 1.1, True, [0,1,2], (1,2),
        {0,1}, {'nome': 'Luiz'},
         
]

for i in lista:
    if isinstance(i,set):
        print('set')
        i.add(4)
        print(i, isinstance(i,set))
        
    elif isinstance(i,str):
        print('str')
        print(i.upper(), isinstance(i,set))
        
    elif isinstance(i, (int,float)):
        print('num')
        print(i, i * 2)
    else:
        print('outro')
        print(i)
