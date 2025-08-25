"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
"""

x = 1  # Escopo global

def escopo():
    global x  # Declara que x é a variável global vai da 22
    x = 22 
    
    def outra_funcao():
        #global x  # Declara que x é a variável global vai da 11
        x = 11
        y = 2
        print(x,y)
        
    outra_funcao()
    print(x)
    
print(x),
escopo(),
print(x)