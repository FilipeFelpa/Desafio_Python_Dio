# Criar um sistema bancário com três operações: Depósito, saque e extrato
# Depósito: Somente valores positivos, para uma só conta
# Saque: Limite diário de três saque, limite de R$ 500,00 por saque
# Extrato: Deve listar os depósitos e saques, se estiver em branco deve exibir a mensagem: Não foram realizadas movimentações...
# Valores exibidos R$ xxx.xx

def menu():
    menu = """
    *********Bem-vindo ao Banco DIO*********\n
    [1]\tDepósito
    [2]\tSaque
    [3]\tExtrato
    [4]\tSair
    O que seja realiza => """
    return int(input(menu))

#def deposito(saldo1):
#    saldo_temp = saldo1
#    valor_depositado = float(input("Informe o valor a ser depositado: "))
#    if valor_depositado > 0:
#        saldo_temp = saldo_temp + valor_depositado
#        global extrato += f"Depósito: R$ {valor_depositado:.2f}\n"
#        return saldo_temp
#    else:
#        print("Valor informado é invalido, favor preencher com um valor valido")
#        menu()
    
#def saque(saldo,quant_limite_saque,limite):
#    valor = float(input("Quanto deseja sacar?: "))
#    passou_limite = valor > limite
#    passou_saldo = valor > saldo
#    limite_saque = quant_limite_saque == 0

#    if passou_saldo:
#        print("Saldo insuficiente!")
#    elif passou_limite:
#        print("Solicitado acima do limite permitido! Tente novamente")
#    elif limite_saque:
#        print("Foi excedido se limite de saque diário!")
#    elif valor > 0:
#        saldo -= valor
#        global extrato += f"Saque: R$ {valor:.2f}\n"
#        return saldo
#    else:
#        print("OPeração não reconhecida!")

quant_limite_saque = 3
limite = 500
saldo = 0.0
extrato = ""

while True:
    resultado = menu()
    if resultado == 1:
#       saldo = deposito(saldo)
        valor_depositado = float(input("Informe o valor a ser depositado: "))
        if valor_depositado > 0:
            saldo += valor_depositado
            extrato += f"Depósito: R$ {valor_depositado:.2f}\n"
            print("Deposito realizado!")
        else:
            print("Valor informado é invalido, favor preencher com um valor valido")
    elif resultado == 2:
#        saldo = saque(saldo,quant_limite_saque,limite)
#        quant_limite_saque -= 1
        valor = float(input("Quanto deseja sacar?: "))
        passou_limite = valor > limite
        passou_saldo = valor > saldo
        limite_saque = quant_limite_saque == 0

        if passou_saldo:
            print("Saldo insuficiente!")
        elif passou_limite:
            print("Solicitado acima do limite permitido! Tente novamente")
        elif limite_saque:
            print("Foi excedido se limite de saque diário!")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            print("Saque realizado")
            quant_limite_saque -= 1
        else:
            print("OPeração não reconhecida!")
    elif resultado == 3:
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
    elif resultado == 4:
        break
    else:
        print("Operação inválida, tente novamente!")