import json
import os

def carregar_tarefas(nome_arquivo):
    if os.path.exists(nome_arquivo):
        with open(nome_arquivo, 'r') as f:
            return json.load(f)
    return []

def salvar_tarefas(tarefas, nome_arquivo):
    with open(nome_arquivo, 'w') as f:
        json.dump(tarefas, f)

def adicionar_tarefa(tarefas, tarefa):
    tarefas.append(tarefa)

def listar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
    else:
        for i, tarefa in enumerate(tarefas, 1):
            print(f"{i}. {tarefa}")

def remover_tarefa(tarefas, indice):
    if 0 <= indice < len(tarefas):
        tarefas.pop(indice)
        print("Tarefa removida com sucesso!")
    else:
        print("Índice inválido.")

def main():
    nome_arquivo = 'tarefas.json'
    tarefas = carregar_tarefas(nome_arquivo)

    while True:
        print("\nGerenciador de Tarefas")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Remover Tarefa")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            tarefa = input("Digite a tarefa: ")
            adicionar_tarefa(tarefas, tarefa)
            salvar_tarefas(tarefas, nome_arquivo)
            print("Tarefa adicionada com sucesso!")
        elif opcao == '2':
            listar_tarefas(tarefas)
        elif opcao == '3':
            listar_tarefas(tarefas)
            try:
                indice = int(input("Digite o número da tarefa a ser removida: ")) - 1
                remover_tarefa(tarefas, indice)
                salvar_tarefas(tarefas, nome_arquivo)
            except ValueError:
                print("Por favor, insira um número válido.")
        elif opcao == '4':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
