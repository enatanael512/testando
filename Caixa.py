saldo = 1000.00

while True:
    print("\n===== CAIXA ELETRÔNICO =====")
    print("1 - Consultar saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print(f"Saldo atual: R$ {saldo:.2f}")

    elif opcao == "2":
        deposito = float(input("Digite o valor do depósito: R$ "))
        if deposito > 0:
            saldo += deposito
            print(f"Depósito realizado com sucesso!")
            print(f"Novo saldo: R$ {saldo:.2f}")
        else:
            print("Valor inválido!")

    elif opcao == "3":
        saque = float(input("Digite o valor do saque: R$ "))
        if saque <= 0:
            print("Valor inválido!")
        elif saque > saldo:
            print("Saldo insuficiente!")
        else:
            saldo -= saque
            print(f"Saque realizado com sucesso!")
            print(f"Novo saldo: R$ {saldo:.2f}")

    elif opcao == "4":
        print("Obrigado por utilizar o caixa eletrônico!")
        break

    else:
        print("Opção inválida! Tente novamente.")