lista_compras = []

while True:
    print("\n===== LISTA DE COMPRAS =====")
    print("1 - Adicionar produto")
    print("2 - Listar produtos")
    print("3 - Remover produto")
    print("4 - Encerrar")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        produto = input("Digite o nome do produto: ")
        lista_compras.append(produto)
        print("Produto adicionado com sucesso!")

    elif opcao == "2":
        if len(lista_compras) == 0:
            print("A lista está vazia.")
        else:
            print("\nProdutos na lista:")
            for produto in lista_compras:
                print("-", produto)

    elif opcao == "3":
        produto = input("Digite o nome do produto para remover: ")
        if produto in lista_compras:
            lista_compras.remove(produto)
            print("Produto removido com sucesso!")
        else:
            print("Produto não encontrado na lista.")

    elif opcao == "4":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida! Tente novamente.")