from Armazenador import Armazenador

class ArmazenadorArquivo(Armazenador):

    def salvar(self, dado):
        print(f"Salvando '{dado}' em arquivo local.")