from io import StringIO
import sys
import textwrap


def deposito(saldo, valor_deposito, lista_extrato, /):
        OPERACAO = "Depósito"
        if valor_deposito > 0:
            saldo += valor_deposito
            lista_extrato.append([OPERACAO, valor_deposito])
            return saldo


def saque(*,saldo, valor_saque, lista_extrato, numero_saques, LIMITE_SAQUES, limite):
        OPERACAO = "Saque"
        if valor_saque <= limite and numero_saques < LIMITE_SAQUES and saldo >= valor_saque:
            numero_saques += 1
            saldo -= valor_saque
            lista_extrato.append([OPERACAO, valor_saque])
            return saldo
        elif valor_saque > limite:
            print("ERRO: Limite de saque é de R$500 reais")
        elif numero_saques == 3:
            print("ERRO: Limite de números de saques atingido")
        elif saldo < valor_saque:
            print("Saldo insuficiente")

def extrato(saldo, lista_extrato):
        output_buffer = StringIO()
        sys.stdout = output_buffer

        print("Extrato".center(30 , "="))
        for operacoes in lista_extrato:
            print(f"\n{operacoes[0]} - R$ {operacoes[1]:.2f}")
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print("=".center(30, "="))

        sys.stdout = sys.__stdout__
        extrato_completo = output_buffer.getvalue()

        return extrato_completo

def criar_usuario(nome, data_nascimento, cpf, endereco, usuarios):
    usuario = filtra_usuarios(cpf, usuarios)
    if usuario:
        return "Usuário com CPF já existente"
    else:
        usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "endereco": endereco, "cpf": cpf})
        return "Usuário Criado!"


def filtra_usuarios(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(cpf, usuarios, contas, agencia):
    usuario = filtra_usuarios(cpf, usuarios)
    if usuario:
        numero_conta = len(contas) + 1
        contas.append({"agencia": agencia, "usuario": usuario, "numero_conta": numero_conta})
        return "Conta Criada com sucesso!"
    else:
        return "Usuário não encontrado"


def retorna_usuarios(usuarios):
    for usuario in usuarios:
        print(textwrap.dedent(f""" 
                    CPF: {usuario['cpf']}
                    Nome: {usuario['nome']}
                    Data de Nascimento: {usuario['data_nascimento']}
                    Endereço {usuario['endereco']}\n
                """))
        print("=" * 100)

def retorna_contas(contas):
    for conta in contas:
        print(textwrap.dedent(f"""
                    Agencia: {conta['agencia']}
                    Títular: {conta['usuario']['nome']} 
                    Número da conta: {conta['numero_conta']}\n
                """))
        print("=" * 100)


def menu():
        menu = """

        [1] Depositar
        [2] Sacar
        [3] Extrato
        [4] Cadastrar usuário
        [5] Criar conta
        [6] Lista usuários
        [7] Lista contas

        [0] Sair

        => """
        return input(textwrap.dedent(menu))


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    lista_extrato = []
    numero_saques = 0
    usuarios = []
    contas = []



    while True:

        opcao = menu()
        if opcao == "1":
            valor = float(input("Valor a ser depositado: "))
            saldo = deposito(saldo, valor, lista_extrato)
            print(extrato(saldo, lista_extrato))

        elif opcao == "2":
            valor = float(input("Valor a ser Sacado: "))
            saldo = saque(saldo=saldo, valor_saque=valor, lista_extrato=lista_extrato, numero_saques=numero_saques, LIMITE_SAQUES=LIMITE_SAQUES, limite=limite)
            print(extrato(saldo, lista_extrato))

        elif opcao == "3":
            print(extrato(saldo, lista_extrato=lista_extrato))

        elif opcao == "4":
            cpf = input("CPF: ")
            nome = input("Nome: ")
            data_nascimento = input("Data de nascimento: ")
            endereco = input("Endereço (logradouro, nro - bairro - cidade/sigla estado): ")
            print(criar_usuario(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco, usuarios=usuarios))

        elif opcao == "5":
            cpf = input("CPF do usuário: ")
            print(criar_conta(cpf=cpf, usuarios=usuarios, contas=contas, agencia=AGENCIA))

        elif opcao == "6":
            retorna_usuarios(usuarios=usuarios)
            
        elif opcao == "7":
            retorna_contas(contas)

        elif opcao == "0":
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada")

main()

# print(saque(saldo=saldo, lista_extrato=lista_extrato, numero_saques=numero_saques, LIMITE_SAQUES=LIMITE_SAQUES, funcao=extrato))
# print(deposito(saldo, lista_extrato, extrato))
# print(extrato(saldo, lista_extrato=lista_extrato))