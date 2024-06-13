
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu) 
    if opcao == "d":
        valor_deposito = float(input("Valor para depósito: "))
        if valor_deposito <= 0:
            print("Falha na operação! Valor de depósito inválido!")
            continue
        saldo += valor_deposito
        extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
    elif opcao == "s":
        valor_saque = float(input("Informe o valor de saque: "))
        excedeu_saldo =  valor_saque > saldo
        excedeu_limite = valor_saque > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        if excedeu_saldo:
            print("Operação falhou! Não há saldo suficiente!")
        elif excedeu_limite:
            print("Operação falhou! Valor do saque excede o limite!")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido!")
        elif valor_saque > 0:
            saldo -= valor_saque
            numero_saques += 1
            extrato += f"Saque: R$ {valor_saque:.2f}\n"   
        else:
            print("Falha na operação! Valor de saque inválido!")       
    elif opcao == "e":
        print(" Extrato ".center(40, '='))
        print("\nNão foram realizadas movimentações.\n" if not extrato else extrato)
        print("*" * 40 + "\n")
        print(f"Saldo de R$ {saldo:.2f}\n")
        print("*" * 40 + "\n")
    elif opcao == "q":
        confirmacao = input("Deseja realmente sair da aplicação? [1-sair ou 2-continuar]: ")
        while confirmacao != "1" and confirmacao != "2":
             print("Opção inválida!")
             confirmacao = input("Deseja realmente sair da aplicação? [1-sair ou 2-continuar]: ")
        if confirmacao == "1":
            break
        elif confirmacao == "2":
            continue
    else:
       print("Operação inválida, por favor selecione novamente a operação desejada.") 