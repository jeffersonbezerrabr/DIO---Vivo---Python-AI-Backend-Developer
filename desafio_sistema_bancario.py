
limite_saque_diario = 3
saques_realizados = 0
limite_por_saque = 500
saldo = 0
extrato = ""



while True:
    menu = input("""

Escolha uma das opções abaixo:

[S]acar
[D]epositar
[E]xtrato
[F]inalizar

Opção: """).upper()
    
    if menu == "D":
        valor_deposito = input("Quanto deseja depositar? R$ ")
        try:
            float_valor_deposito = float(valor_deposito)
            if float_valor_deposito < 0:
                print("Precisa informar um valor positivo")
                
            else:
                saldo += float_valor_deposito
                extrato += f"Deposito realizado no valor de R$ {float_valor_deposito:.2f}\n"
        except ValueError:
            print("Precisa digitar um valor númerico positivo.")
    
    elif menu == "S":
        if limite_saque_diario > 0:
            valor_saque = input("Quanto deseja sacar? R$ ")
            try:
                float_valor_saque = float(valor_saque)
                if float_valor_saque > 500:
                    print("Seu limite por saque é de R$ 500,00")
                    print("Digite um valor menor ou igual a 500")
                    
                elif float_valor_saque <= 500 and float_valor_saque <= saldo:
                    saldo -= float_valor_saque
                    limite_saque_diario -= 1
                    print(f"Saque realizado no valor de R$ {float_valor_saque:.2f}\n")
                    print(f"Saldo atual: R$ {saldo:.2f}\n")
                    print(f"Quantidade de saques diarios: {limite_saque_diario} \n")
                    extrato += f"Saque realizado no valor de R$ {float_valor_saque:.2f}\n"
                
                elif float_valor_saque <= 500 and float_valor_saque > saldo:
                    print("Saldo insuficiente")
            except ValueError:
                print("Digite um valor númerico positivo.")
        else:
            print("Você atingiu o limite de saques diarios")
                
    elif menu == "E":
        if extrato == '':
            print("Você não tem movimentações")
            print(f"Saldo atual: R$ {saldo:.2f}")
            print(f"Quantidade de saques diarios: {limite_saque_diario} \n")
        else:
            print(f"{extrato}")
            print()
            print(f"Quantidade de saques diarios: {limite_saque_diario} \n")
            print(f"Saldo atual: R$ {saldo:.2f}")
            
    elif menu == "F":
        print("Encerrando...")
        break
    
    else:
        print("Digite uma das opções informadas: [S], [D], [E], [F]\n")

print("Obrigado por utilizar nosso sistema bancário.")
    