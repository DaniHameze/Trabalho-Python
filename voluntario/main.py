# Lista para armazenar voluntários e alimentos
voluntarios = []
alimentos = []

# Funções
def adicionar_voluntario():
    nome = input("Digite o nome do voluntário: ")
    voluntarios.append(nome)
    print(f"Voluntário {nome} adicionado com sucesso!")

def adicionar_alimento():
    alimento = input("Digite o nome do alimento: ")
    alimentos.append(alimento)
    print(f"Alimento {alimento} adicionado com sucesso!")

def listar_voluntarios():
    if voluntarios:
        print("\nLista de voluntários:")
        for i, nome in enumerate(voluntarios, 1):
            print(f"{i}. {nome}")
    else:
        print("Nenhum voluntário cadastrado ainda.")

def listar_alimentos():
    if alimentos:
        print("\nLista de alimentos:")
        for i, alimento in enumerate(alimentos, 1):
            print(f"{i}. {alimento}")
    else:
        print("Nenhum alimento cadastrado ainda.")

# Menu principal
def menu():
    while True:
        print("\nSistema de Cadastro de Voluntários e Alimentos")
        print("1. Adicionar Voluntário")
        print("2. Adicionar Alimento")
        print("3. Listar Voluntários")
        print("4. Listar Alimentos")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar_voluntario()
        elif opcao == '2':
            adicionar_alimento()
        elif opcao == '3':
            listar_voluntarios()
        elif opcao == '4':
            listar_alimentos()
        elif opcao == '5':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida, tente novamente.")

# Executar o menu
if __name__ == "__main__":
    menu()
