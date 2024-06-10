class Extrato:
    def __init__(self):
        self.transacoes = []

def extrato(self, numeroConta):
    print(f"Extrato: {numeroConta} \n")

    for variavel in self.transacoes:
        print(f"{variavel[0]:15s} {variavel[1]:10.2f} {variavel[2]:10s} {variavel[3].strftime('%d/%b/%y')}")
