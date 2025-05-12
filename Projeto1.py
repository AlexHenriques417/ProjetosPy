nome = str(input("Digite o seu nome: "))
instituicao = str(input("Digite o nome de sua Instituição de ensino: "))
idade = str(input("Digite a sua idade: "))

print("Nome: {} | Instituição: {} | Idade: {}".format(nome, instituicao, idade))

def menu():
    print("=== Escolha da Disciplina ===")
    print("1 - Portugês")
    print("2- Matemática")
    print("3 - Geografia")
    print("4 - História")
    print("5 - Ciências")
    print("6 - Sair")

while True:
    menu()
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        print("Portugês")
        break
    elif opcao == 2:
        print("Matemática")
        break
    elif opcao == 3:
        print("Geografia")
        break
    elif opcao == 4:
        print("História")
        break
    elif opcao == 5:
        print("Ciências")
        break
    elif opcao == 6:
        print("Sair")
        import sys
        sys.exit()
    else:
        print("Opção Inválida")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3
print("A média é de: {}".format(media))

if media >= 7.0:
    print("Aprovado")
elif media > 5 and media < 7:
    print("Recuperação")

    escolha = int(input("Escolha o dia da recuperação(1-3): "))

    match escolha:
        case 1:
            print("Segunda")
        case 2: 
            print("Terça")
        case 3:
            print("Quarta")
        case _:
            print("Opção inválida")
else:
    print("Reprovado")