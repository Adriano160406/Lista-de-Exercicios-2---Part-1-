from Boleto import Boleto
from Etiqueta import Etiqueta
from RelatorioSimples import RelatorioSimples
from ProcessarImpressão import processar_impressao

boleto = Boleto("123456", 250)
etiqueta = Etiqueta("Adriano", "Rua das Flores")
relatorio = RelatorioSimples("Relatório Mensal")

processar_impressao(boleto)
print()

processar_impressao(etiqueta)
print()

processar_impressao(relatorio)

"""1. Onde está o contrato nesse caso?
O contrato está no protocolo Imprimivel.

2. Por que as classes podem funcionar sem herdar explicitamente do protocolo?
Porque o importante é que elas tenham o método imprimir().

3. Esse caso se aproxima mais de ABC ou de duck typing?
Esse caso se aproxima mais de duck typing.

4. Qual a principal diferença entre esse caso e o da Questão 1?
Na Questão 1 as classes precisavam herdar da classe abstrata.
Nesse caso, as classes não precisam herdar do protocolo, apenas implementar o método esperado."""