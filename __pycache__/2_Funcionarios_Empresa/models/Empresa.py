class Empresa:
    def __init__(self, nome):
        self.nome = nome
        self.lista_funcionarios = []

    def adicionar_funcionario(self, funcionario):
        self.lista_funcionarios.append(funcionario)

    def listar_funcionarios(self):
        print(f"\nFuncionários da empresa {self.nome}:")

        for funcionario in self.lista_funcionarios:
            print(funcionario.nome)

    def mostrar_folha_pagamento(self):
        print(f"\nFolha de pagamento da empresa {self.nome}:")

        for funcionario in self.lista_funcionarios:
            print(f"{funcionario.nome}: R$ {funcionario.calcular_pagamento()}")