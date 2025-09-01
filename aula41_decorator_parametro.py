# Decoradores com parametros

def decoradora(func):
    print('Decoradora 1')
    
    def aninhada(*args, **Kwargs):
        print('Aninhada')
        res = func(*args, **Kwargs)
        return res
    return aninhada

@decoradora
def soma(x, y):
    return x + y

dez_mais_cinco = soma(10, 5)
print(dez_mais_cinco)
