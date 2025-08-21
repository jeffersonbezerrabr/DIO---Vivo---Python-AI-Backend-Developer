
limite_saque_diario = 3
saques = 0
limite_por_saque = 500
saldo = 0
extrato = ""
usuarios = []
contas = []
AGENCIA = "0001"


def sacar(*, saldo, extrato, limite_saque_diario, limite_por_saque, valor_saque):
    if limite_saque_diario > 0:
            try:
                float_valor_saque = float(valor_saque)
                if float_valor_saque > limite_por_saque:
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
    return saldo, extrato, limite_saque_diario

def depositar(valor_deposito, saldo, extrato, /,):
    try:
        float_valor_deposito = float(valor_deposito)
        if float_valor_deposito <= 0:
                print("Precisa informar um valor positivo")
                
        else:
            print(f"R$ {valor_deposito} depositado com sucesso ")
            saldo += float_valor_deposito
            extrato += f"Deposito realizado no valor de R$ {float_valor_deposito:.2f}\n"
    except ValueError:
        print("Precisa digitar um valor númerico positivo.")
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato, limite_saque_diario):
    if extrato == '':
        print("Você não tem movimentações")
        print(f"Saldo atual: R$ {saldo:.2f}")
        print(f"Quantidade de saques diarios: {limite_saque_diario} \n")
    else:
        print(f"{extrato}")
        print()
        print(f"Quantidade de saques diarios: {limite_saque_diario} \n")
        print(f"Saldo atual: R$ {saldo:.2f}")
    
    return saldo, extrato

def criar_usuario(usuarios):
    while True:
        cpf = input("Informe o CPF(Apenas números): ")
        if not cpf.isnumeric():
            print("Digite apenas números\n")
            continue  # volta para o início do loop dentro da função
        
        usuario = consulta_usuario(cpf, usuarios)
        if usuario:
            print("Já existe um usuário cadastrado com esse CPF!\n")
            return  # sai da função e volta para o menu principal
        break  # sai do loop quando o CPF for válido e não existir

    nome = input("Informe seu nome completo: ")
    data_nascimento = input("Informe sua data de nascimento [dd-mm-aaaa]: ")
    endereco = input("Informe o endereço [Nome da rua, número - bairro - Cidade/UF]: ")
    
    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    })
    
    print("Usuário cadastrado com sucesso!\n")

def consulta_usuario(cpf, usuarios):
    usuarios_consultados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_consultados[0] if usuarios_consultados else None

def criar_conta(agencia, conta_corrente, usuarios):
    cpf = input("Informe o CPF(Apenas números): ")
    usuario = consulta_usuario(cpf, usuarios)
    
    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "conta_corrente": conta_corrente, "cpf": usuario["cpf"]}
    
    print("Usuário não encontrado! Encerrando criação de conta...")
    
def listar_contas(contas, usuarios):
    if len(contas) == 0:
        print("Nenhuma conta cadastrada")
    else:
        for conta in contas:
            usuario = consulta_usuario(conta["cpf"], usuarios)
            print(f"\nAgência: {conta['agencia']}\nConta: {conta['conta_corrente']}\nTitular: {usuario['nome']}\n")
            print("*"*15)
            print()
    print("*=" * 30)

while True:
    menu_0 = input("""

Escolha uma das opções abaixo:

[C]adastrar usuario
[F]inalizar

Opção: """).upper()
    
        
    if menu_0 == "C":
        criar_usuario(usuarios)
        break

    elif menu_0 == "F":
        print("Encerrando...")
        exit()    
    else:
        print("Digite uma das opções informadas: [C], [F]\n")


while True:
    menu_1 = input("""

Escolha uma das opções abaixo:

[N]ova Conta
[F]inalizar

Opção: """).upper()
    
    if menu_1 == "N":
        conta_corrente = len(contas) + 1
        conta = criar_conta(AGENCIA, conta_corrente, usuarios)
        
        if conta:
            contas.append(conta)
            break
    
    elif menu_1 == "F":
        print("Encerrando...")
        exit()    
    else:
        print("Digite uma das opções informadas: [N], [F]\n")

while True:
    menu_2 = input("""

Escolha uma das opções abaixo:

[S]acar
[D]epositar
[E]xtrato
[N]ova Conta
[L]istar Contas
[C]adastrar usuario
[F]inalizar

Opção: """).upper()
    
    if menu_2 == "D":
        valor_deposito = input("Quanto deseja depositar? R$ ")
        saldo, extrato = depositar(valor_deposito, saldo, extrato)
    
    elif menu_2 == "S":
        valor_saque = input("Quanto deseja sacar? R$ ")
        saldo, extrato, limite_saque_diario =sacar(
            saldo=saldo,
            extrato=extrato,
            limite_saque_diario=limite_saque_diario,
            limite_por_saque=limite_por_saque,
            valor_saque=valor_saque
        )
                
    elif menu_2 == "E":
         exibir_extrato(saldo, extrato=extrato, limite_saque_diario=limite_saque_diario)
         
    elif menu_2 == "N":
        conta_corrente = len(contas) + 1
        conta = criar_conta(AGENCIA, conta_corrente, usuarios)
        
        if conta:
            contas.append(conta)
            
    elif menu_2 == "L":
        listar_contas(contas, usuarios)
        
    elif menu_2 == "C":
        criar_usuario(usuarios)        

            
    elif menu_2 == "F":
        print("Encerrando...")
        break
    
    else:
        print("Digite uma das opções informadas: [S], [D], [E], [F]\n")

print("Obrigado por utilizar nosso sistema bancário.")
    