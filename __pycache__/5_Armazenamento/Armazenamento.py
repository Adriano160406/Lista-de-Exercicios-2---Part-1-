from abc import ABC, abstractmethod
from typing import Protocol


class Armazenador(ABC):

    @abstractmethod
    def salvar(self, dado):
        pass


class ArmazenadorArquivo(Armazenador):

    def salvar(self, dado):
        print(f"Salvando '{dado}' em arquivo local.")


class ArmazenadorBanco(Armazenador):

    def salvar(self, dado):
        print(f"Salvando '{dado}' no banco de dados.")


class Salvavel(Protocol):

    def salvar(self, dado):
        pass


class ArmazenadorNuvem:

    def salvar(self, dado):
        print(f"Salvando '{dado}' na nuvem.")


def executar_salvamento_formal(armazenador, dado):
    armazenador.salvar(dado)


def executar_salvamento_flexivel(objeto, dado):
    objeto.salvar(dado)


arquivo = ArmazenadorArquivo()
banco = ArmazenadorBanco()
nuvem = ArmazenadorNuvem()

print("=== Salvamento Formal ===")
executar_salvamento_formal(arquivo, "dados.txt")
executar_salvamento_formal(banco, "clientes")

print("\n=== Salvamento Flexível ===")
executar_salvamento_flexivel(arquivo, "dados.txt")
executar_salvamento_flexivel(banco, "clientes")
executar_salvamento_flexivel(nuvem, "backup")


"""
1. Em qual parte há contrato por herança?
O contrato por herança está na classe abstrata Armazenador.

2. Em qual parte há contrato estrutural?
O contrato estrutural está no protocolo Salvavel.

3. Qual abordagem é mais rígida?
A abordagem usando ABC é mais rígida.

4. Qual abordagem é mais flexível?
A abordagem usando Protocol é mais flexível.

5. Em qual situação ABC faz mais sentido? E em qual Protocol faz mais sentido?
ABC faz mais sentido quando queremos obrigar as classes a seguirem uma hierarquia.
Protocol faz mais sentido quando queremos aceitar qualquer objeto que tenha o método necessário.
"""