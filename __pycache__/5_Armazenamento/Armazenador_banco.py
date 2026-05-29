from Armazenador import Armazenador

class ArmazenadorBanco(Armazenador):

    def salvar(self, dado):
        print(f"Salvando '{dado}' no banco de dados.")