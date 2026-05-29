from abc import ABC, abstractmethod


class Funcionario(ABC):
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")

    @abstractmethod
    def calcular_pagamento(self):
        pass


class FuncionarioAssalariado(Funcionario):
    def __init__(self, nome, cpf, salario_mensal):
        super().__init__(nome, cpf)
        self.salario_mensal = salario_mensal

    def calcular_pagamento(self):
        return self.salario_mensal


class FuncionarioHorista(Funcionario):
    def __init__(self, nome, cpf, horas_trabalhadas, valor_hora):
        super().__init__(nome, cpf)
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_hora = valor_hora

    def calcular_pagamento(self):
        return self.horas_trabalhadas * self.valor_hora


class FuncionarioComissionado(Funcionario):
    def __init__(self, nome, cpf, total_vendas, percentual_comissao):
        super().__init__(nome, cpf)
        self.total_vendas = total_vendas
        self.percentual_comissao = percentual_comissao

    def calcular_pagamento(self):
        return self.total_vendas * (self.percentual_comissao / 100)


class Empresa:
    def __init__(self, nome):
        self.nome = nome
        self.lista_funcionarios = []

    def adicionar_funcionario(self, funcionario):
        self.lista_funcionarios.append(funcionario)

    def listar_funcionarios(self):
        print(f"\nFuncionários da empresa {self.nome}:")
        for funcionario in self.lista_funcionarios:
            funcionario.mostrar_dados()
            print()

    def mostrar_folha_pagamento(self):
        print(f"\nFolha de pagamento da empresa {self.nome}:")
        for funcionario in self.lista_funcionarios:
            pagamento = funcionario.calcular_pagamento()
            print(f"{funcionario.nome}: R$ {pagamento:.2f}")


empresa = Empresa("Tech Solutions")

funcionario1 = FuncionarioAssalariado(
    "Carlos",
    "111.111.111-11",
    3500
)

funcionario2 = FuncionarioHorista(
    "Ana",
    "222.222.222-22",
    160,
    25
)

funcionario3 = FuncionarioComissionado(
    "Pedro",
    "333.333.333-33",
    10000,
    10
)

empresa.adicionar_funcionario(funcionario1)
empresa.adicionar_funcionario(funcionario2)
empresa.adicionar_funcionario(funcionario3)

empresa.listar_funcionarios()

print("\nFolha de pagamento:")
empresa.mostrar_folha_pagamento()


"""
1. Qual é a superclasse da hierarquia?
A superclasse da hierarquia é a classe Funcionario.

2. Quais são as subclasses?
As subclasses são:
- FuncionarioAssalariado
- FuncionarioHorista
- FuncionarioComissionado

3. Onde ocorre sobrescrita?
A sobrescrita ocorre no método calcular_pagamento(),
pois cada subclasse implementa esse método de forma diferente.

4. Onde ocorre polimorfismo?
O polimorfismo ocorre no método mostrar_folha_pagamento(),
quando o sistema percorre a lista de funcionários e chama
calcular_pagamento() para cada objeto.

5. Qual a vantagem de usar ABC nesse caso?
A vantagem é garantir que todas as subclasses implementem
o método calcular_pagamento(), deixando o sistema mais organizado.
"""