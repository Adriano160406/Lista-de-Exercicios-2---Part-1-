from Plataforma import Plataforma
from Vídeo import Video
from Podcast import Podcast
from TextoNarrado import TextoNarrado

plataforma = Plataforma("Educa Play")

video1 = Video("Aula de Python", "20 minutos", "1080p")
podcast1 = Podcast("Conversa sobre POO", "35 minutos", "Professor Alternei")
texto1 = TextoNarrado("Resumo de Programação", "10 minutos", "Português")

plataforma.adicionar_midia(video1)
plataforma.adicionar_midia(podcast1)
plataforma.adicionar_midia(texto1)

plataforma.listar_midias()

print("\nReproduzindo todas as mídias:")
plataforma.reproduzir_todas()

"""1. Qual é a classe abstrata do sistema?
A classe abstrata do sistema é a classe Midia.

2. Onde aparece a hierarquia?
A hierarquia aparece quando as classes Video, Podcast e TextoNarrado herdam da classe Midia.

3. Onde aparece o polimorfismo?
O polimorfismo aparece no método reproduzir_todas(), pois ele percorre a lista de mídias e chama o método reproduzir() em cada objeto.

4. Por que Midia não deveria ser instanciada diretamente?
Porque Midia é uma classe muito geral e serve apenas como base para as outras mídias. Cada tipo de mídia precisa ter sua própria forma de reprodução."""
