from abc import ABC, abstractmethod


class Midia(ABC):
    def __init__(self, titulo, duracao):
        self.titulo = titulo
        self.duracao = duracao

    def mostrar_info(self):
        print(f"Título: {self.titulo}")
        print(f"Duração: {self.duracao}")

    @abstractmethod
    def reproduzir(self):
        pass


class Video(Midia):
    def __init__(self, titulo, duracao, resolucao):
        super().__init__(titulo, duracao)
        self.resolucao = resolucao

    def reproduzir(self):
        print(f"Reproduzindo vídeo '{self.titulo}' em {self.resolucao}.")


class Podcast(Midia):
    def __init__(self, titulo, duracao, apresentador):
        super().__init__(titulo, duracao)
        self.apresentador = apresentador

    def reproduzir(self):
        print(f"Reproduzindo podcast '{self.titulo}' apresentado por {self.apresentador}.")


class TextoNarrado(Midia):
    def __init__(self, titulo, duracao, idioma):
        super().__init__(titulo, duracao)
        self.idioma = idioma

    def reproduzir(self):
        print(f"Reproduzindo texto narrado '{self.titulo}' no idioma {self.idioma}.")


class Plataforma:
    def __init__(self, nome):
        self.nome = nome
        self.lista_midias = []

    def adicionar_midia(self, midia):
        self.lista_midias.append(midia)

    def listar_midias(self):
        print(f"\nMídias da plataforma {self.nome}:")
        for midia in self.lista_midias:
            midia.mostrar_info()
            print()

    def reproduzir_todas(self):
        print(f"\nReproduzindo mídias da plataforma {self.nome}:")
        for midia in self.lista_midias:
            midia.reproduzir()


plataforma = Plataforma("Educa Play")

video1 = Video("Aula de Banco de Dados", "20 minutos", "1080p")
podcast1 = Podcast("Conversa sobre POO", "35 minutos", "Professor Alternei")
texto1 = TextoNarrado("Resumo de Programação", "10 minutos", "Português")

plataforma.adicionar_midia(video1)
plataforma.adicionar_midia(podcast1)
plataforma.adicionar_midia(texto1)

plataforma.listar_midias()

print("\nReproduzindo todas as mídias:")
plataforma.reproduzir_todas()


"""
1. Qual é a classe abstrata do sistema?
A classe abstrata do sistema é a classe Midia.

2. Onde aparece a hierarquia?
A hierarquia aparece quando as classes Video, Podcast e TextoNarrado herdam da classe Midia.

3. Onde aparece o polimorfismo?
O polimorfismo aparece no método reproduzir_todas(), pois ele percorre a lista de mídias e chama o método reproduzir() em cada objeto.

4. Por que Midia não deveria ser instanciada diretamente?
Porque Midia é uma classe muito geral e serve apenas como base para as outras mídias. Cada tipo de mídia precisa ter sua própria forma de reprodução.
"""