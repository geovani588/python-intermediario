import os

todo = []
pilha_refazer = []

def cls():
    os.system("cls" if os.name == "nt" else "clear")

def listar():
    print("\nTODO:", todo if todo else "(vazio)")
    print("Desfeitos:", pilha_refazer if pilha_refazer else "(vazio)\n")

while True:
    cls()  # limpa a tela antes de mostrar o menu
    print("=== MENU ===")
    print("1 - Adicionar tarefa")
    print("2 - Desfazer")
    print("3 - Refazer")
    print("4 - Listar tarefas")
    print("5 - Sair")

    escolha = input("Escolha uma opção: ").strip()

    match escolha:
        case "1":
            tarefa = input("Digite a tarefa: ").strip()
            if tarefa:
                todo.append(tarefa)
                pilha_refazer.clear()
                print(f"Adicionado: {tarefa}")
            else:
                print("Tarefa vazia não pode ser adicionada.")
            input("\nPressione Enter para continuar...")

        case "2":
            if todo:
                tarefa = todo.pop()
                pilha_refazer.append(tarefa)
                print(f"Desfeito: {tarefa}")
            else:
                print("Nada para desfazer")
            input("\nPressione Enter para continuar...")

        case "3":
            if pilha_refazer:
                tarefa = pilha_refazer.pop()
                todo.append(tarefa)
                print(f"Refeito: {tarefa}")
            else:
                print("Nada para refazer")
            input("\nPressione Enter para continuar...")

        case "4":
            listar()
            input("\nPressione Enter para continuar...")

        case "5":
            print("Até mais!")
            break

        case _:
            print("Opção inválida, tente novamente.")
            input("\nPressione Enter para continuar...")
