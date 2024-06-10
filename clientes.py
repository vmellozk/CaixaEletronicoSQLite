class Cliente:
    def __init__(self, cpf, nome, endereco):
        self.cpf = cpf
        self.nome = nome
        self.endereco = endereco

    def __eq__(self, outro):
        if isinstance(outro, Cliente):
            return self.cpf == outro.cpf
        return False
