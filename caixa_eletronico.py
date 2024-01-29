saldo_atual = 1500
saque_diario = 3
extrato = []

while True:
    print("\n--  BANCO DA MOEDA PYTONICA ---")

    num = int(input('OPCOES:\n'
                    '1 - Deposito\n'
                    '2 - Saque\n'
                    '3 - Extrato\n'
                    '0 - Sair\n'
                    'Digite sua escolha:')) # opcoes do menu

    # DEPOSITO
    if num == 1:
        print(f'\n--- DEPOSITO ---\n')

        while True:
            val_deposito = float(input(f'Digite o valor para deposito:'))

            if val_deposito > 0:
                print(f'Voce deseja depositar R${val_deposito:.2f}')
                conf = str(input(f'Confirme digitando. | (Sim/Não): ')).upper()

                if conf[:1] == "S":
                    print(f'Deposito realizado')
                    saldo_atual += val_deposito
                    ext_deposito = str(f'Deposito: R$ {val_deposito:.2f}')
                    extrato.append(ext_deposito)
                    break

                elif conf[:1] == "N":
                    print(f'Deposito nao realizado')

                else:
                    print(f'Operacao Invalida')

            else:
                print('O valor do depósito deve ser maior que zero.')

    # SAQUE
    elif num == 2:
        print(f'\n--- SAQUE ---\n')

        print(f'Valor Atual disponivel para Saque: R${saldo_atual:.2f}')
        print(f'Saques diponiveis: {saque_diario}\n')

        if saque_diario != 0:
            val_saque = float(input(f'Digite o valor para saque: R$'))
            conf = str(input(f'Voce deseja sacar R$ {val_saque:.2f} | (Sim/Não): ')).upper()

            if conf[:1] == "S":
                if (val_saque > 0 and val_saque <= 500) and (val_saque <= saldo_atual) and (
                        saque_diario > 0 and saque_diario <= 3):
                    print('Saque Autorizado')
                    print(f'O valor de R${val_saque:.2f} foi sacado da sua conta')

                    saldo_atual -= val_saque
                    saque_diario -= 1
                    ext_saque = str(f'Saque: R$ {val_saque:.2f}')
                    extrato.append(ext_saque)

                else:
                    print(f'Saque Nao Autorizado')
                    print('Verifique o valor desejado!')

            elif conf[:1] == "N":
                print(f'Saque nao realizado')
                break

            else:
                print(f'Operacao Invalida')

        else:
            print(f'Quantidade de saques esgotada')
            break

    # EXTRATO
    elif num == 3:
        print(f'\n--- EXTRATO ---\n')

        print(f'Valor atual da conta: R${saldo_atual:.2f}')
        print(f'Quantidade de extratos disponiveis {len(extrato)}\n')

        conf = str(input('Deseja ver os ultimos extratos? (Sim/Não): ')).upper()
        if conf[:1] == "S":
            n = int(input('Escolha a quantidades de extratos exibidos por ultimo:'))
            if n <= len(extrato):
                for i in range(1, n + 1):
                    if i <= len(extrato):
                        print(extrato[-i])
                    else:
                        print("Número de extratos disponíveis é menor que a quantidade desejada.")
                        break
        elif conf[:1] == "N":
            print(f'Operacao Cancelada')
            break
        else:
            print(f'Operacao Invalida')
            break

    # SAIR
    elif num == 0:
        print(f'- Sair -')
        break

    # ERROR
    else:
        print('Opcao Invalida')
