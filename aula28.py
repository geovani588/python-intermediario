# dir, hasatter e getattr em python

string = 'luiz'
metodo = 'upper'

if hasattr(string, 'upper'):
    print('Existe upper')
    print(getattr(string, metodo)())
else:
    print('Nao existe o metodo', metodo)

