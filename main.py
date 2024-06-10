from contas import Conta
from clientes import Cliente
from bancos import Banco

def main():
    banco = Banco()

    cliente4 = Cliente(28247141736, "João", "Rua Monte Alverne, 103")
    cliente3 = Cliente(27144173281, "Mário", "Rua 301 dos Montes, Alverne")

    banco.adicionar_Cliente(cliente4)
    banco.adicionar_Cliente(cliente3)

    banco.criar_Conta(numero = 1, cliente = cliente4, saldo = 70350)
    banco.criar_Conta(numero = 2, cliente = cliente3, saldo = 33450)

if __name__ == "__main__":
    main()
