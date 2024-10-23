# Saque: Limite diário de dez saque, limite de R$ 500,00 por saque
# Extrato: Demonstrar data e hora do saque de todas as transações

from datetime import datetime

import pytz

def menu():
    menu = """
    *********Bem-vindo ao Banco DIO*********\n
    [1]\tDepósito
    [2]\tSaque
    [3]\tExtrato
    [4]\tSair
    O que deseja realizar => """
    return int(input(menu))

def deposito(saldo, extrato):
    valor_depositado = float(input("Informe o valor a ser depositado: "))
    if valor_depositado > 0:
        saldo += valor_depositado
        extrato += f"Depósito: R$ {valor_depositado:.2f} as {DATA_MANAUS}\n"
        return saldo, extrato
    else:
        print("Valor informado é inválido, favor preencher com um valor válido.")
        return saldo, extrato

def saque(saldo, quant_limite_saque, limite, extrato):
    valor = float(input("Quanto deseja sacar?: "))
    passou_limite = valor > limite
    passou_saldo = valor > saldo
    limite_saque = quant_limite_saque == 0

    if passou_saldo:
        print("Saldo insuficiente!")
        return saldo, quant_limite_saque, limite , extrato
    elif passou_limite:
        print("Solicitado acima do limite permitido! Tente novamente.")
        return saldo, quant_limite_saque, limite , extrato
    elif limite_saque:
        print("Foi excedido seu limite de saques diário!")
        return saldo, quant_limite_saque, limite , extrato
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f} as {datetime.today()}\n"
        print("Valor sacado!")
        return saldo, quant_limite_saque - 1, limite , extrato
    else:
        print("Operação não reconhecida!")
        return saldo, quant_limite_saque, limite , extrato

quant_limite_saque = 10
limite = 500
saldo = 0
extrato = ""
# DATA_HORA = datetime.now()
DATA_MANAUS = datetime.now(pytz.timezone("America/Manaus")).replace(microsecond = 0).time()

# data = DATA_HORA.date()
# hora = DATA_HORA.time()
# MASCARA_PTBR = "%d/%M/%Y %H:%M"

while True:
    resultado = menu()
    if resultado == 1:
        saldo, extrato = deposito(saldo, extrato)
    elif resultado == 2:
        saldo, quant_limite_saque, limite, extrato = saque(saldo, quant_limite_saque, limite, extrato)
    elif resultado == 3:
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
    elif resultado == 4:
        break
    else:
        print("Operação inválida, tente novamente!")
