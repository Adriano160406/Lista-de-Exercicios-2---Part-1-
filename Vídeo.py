from Mídia import Midia

class Video(Midia):
    def __init__(self, titulo, duracao, resolucao):
        super().__init__(titulo, duracao)
        self.resolucao = resolucao

    def reproduzir(self):
        print(f"Reproduzindo vídeo '{self.titulo}' em {self.resolucao}.")
        