menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        OPERACAO = "Depósito"
        valor_deposito = float(input("Valor a ser depositado: "))
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato.append([OPERACAO, valor_deposito])
            print("Depósito Realizado")
        else:
            print("Digite um número positivo")


    elif opcao == "2":
        OPERACAO = "Saque"
        valor_saque = float(input("Valor a ser sacado: "))
        if valor_saque <= 500 and numero_saques < LIMITE_SAQUES and saldo >= valor_saque:
            numero_saques += 1
            saldo -= valor_saque
            extrato.append([OPERACAO, valor_saque])
            print("Saque Realizado")
        elif valor_saque > 500:
            print("ERRO: Limite de saque é de R$500 reais")
        elif numero_saques == 3:
            print("ERRO: Limite de números de saques atingido")
        elif saldo < valor_saque:
            print("Saldo insuficiente")

    elif opcao == "3":
        print("Extrato".center(30 , "="))
        for operacoes in extrato:
            print(f"\n{operacoes[0]} - R$ {operacoes[1]:.2f}")
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print("=".center(30, "="))

    elif opcao == "0":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada")