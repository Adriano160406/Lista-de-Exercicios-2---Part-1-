from Empresa import Empresa
from FuncionarioAssalariado import FuncionarioAssalariado
from FuncionarioHorista import FuncionarioHorista
from FuncionarioComissionado import FuncionarioComissionado

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

"""1. Qual é a superclasse da hierarquia?
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
o método calcular_pagamento(), deixando o sistema mais organizado."""