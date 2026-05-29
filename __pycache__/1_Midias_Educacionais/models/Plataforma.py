class Plataforma:
    def __init__(self, nome):
        self.nome = nome
        self.lista_midias = []

    def adicionar_midia(self, midia):
        self.lista_midias.append(midia)

    def listar_midias(self):
        print(f"\nMídias da plataforma {self.nome}:")

        for midia in self.lista_midias:
            print(midia.titulo)

    def reproduzir_todas(self):
        print(f"\nReproduzindo mídias da plataforma {self.nome}:")

        for midia in self.lista_midias:
            midia.reproduzir()