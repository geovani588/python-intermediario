# Try, except, else e finally 

try:
    print('ABRIR ARQUIVO')
    8/0
except ZeroDivisionError:
    print('DIVIDIU ZERO')
except IndexError:
    print('indexERROR')
else:
    print('Nao deu erro')
finally:
    print('FECHAR ARQUIVO')
