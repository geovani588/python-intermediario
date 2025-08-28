# Entregar um valor de cada vez
# Generator expression, Iterables e iterators em Python

# #iterable antigos
# iterable = ['Eu', 'Tenho', '_iter__'] 
# iterator = iter(iterable)# tem __iter__e_next_
# print(next(iterator))# eu
# print(next(iterator))# aki ele vai proximo 'tenho'
# print(next(iterator))# '_iter__'
# #print(next(iterator))# vai da stop dando erro pq n vai ter valores


# Generator recente
# funcoes que sabem pausar em determinado 

import sys
lista = [n for n in range(1000000)]
generator = (n for n in range(1000000))
print(sys.getsizeof(lista))
print (sys.getsizeof(generator))

# for n in generator:
#     print(n)