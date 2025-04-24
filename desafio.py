"""
Desafio!

Fomos contratados por um grande banco para desenvolver o seu novo sistema.
Esse banco deseja modernizar suas operacoes e para isso escolheu a linguagem Python.
Para a 1a versao do sistema devemos implementar apenas 3 operacoes: deposito saque e extrato.

Operacao de deposito: Deve ser possivel depositar valores positivos para a conta bancaria.
A v1 do projeto trabalha apenas com 1 usuario, dessa forma nao precisamos nos preocupar em identificar qual e o numero da agencia e conta bancaria.
Todos os depositos devem ser armazenados em uma variavel e exibidos na operacao extrato.

Operacao de saque: O sistema deve permitir realizar 3 saques diarios com limite maximo de 500.00 reais por saque.
Caso o usuario nao tenha saldo em conta, o sistema deve exibir uma mensagem informando que nao sera possivel sacar o dinheiro por falta de saldo.
Todos os saques devem ser armazenados em uma variavel e exibidos na operacao de extrato.

Operacao de extrato: Essa operacao deve listar todos os depositos e saques realizados na conta.
No fim da listagem deve ser exibido o saldo atual da conta.
Se o extrato estiver em branco, exibir a mensagem: Nao foram realizadas movimentacoes.
Os valores devem ser exibidos utilizando o formato R$ xxx.xxx - Exemplo: 1500.45 = R$ 1500.45
"""

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor que deseja depositar: "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"

        else:
            print("Operacao invalida pois o valor informado nao foi maior que zero.")

    elif opcao == "s":
        valor = float(input("Informe o valor que deseja sacar: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operacao invalida pois o saldo e insuficiente.")

        elif excedeu_limite:
            print("Operacao invalida pois o valor do saque excede o valor limite permitido.")

        elif excedeu_saques:
            print("Operação invalida pois o numero maximo de saques ja foi atingido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou pois o valor informado foi invalido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Nao foram realizadas movimentacoes." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=========================================")

    elif opcao == "q":
        print("Obrigado por usar o nosso Banco! Volte sempre!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")