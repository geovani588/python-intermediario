try:
    a = int(input('Digite o primeiro número: '))
    b = int(input('Digite o segundo número: '))
    
    c = a / b
    print(f"O resultado da divisão é: {c}")
    print("Linha 2")
    
# except ZeroDivisionError as e:
#     print("Erro:", e.__class__.__name__)
#     print("Mensagem:", e)
# except NameError as e:
#     print("Erro:", e.__class__.__name__)
#     print("Mensagem:", e)
except (TypeError, IndexError) as e:
    print("TypeError ou IndexError")
    print("Mensagem:", e)
    print("Nome do erro:", e.__class__.__name__)
except Exception as e:
    print("Erro desconhecido")
    print("Mensagem:", e)

