class CentralNotificacoes:
    def __init__(self):
        self.lista_notificadores = []

    def adicionar_notificador(self, notificador):
        self.lista_notificadores.append(notificador)

    def enviar_para_todos(self, mensagem):

        for notificador in self.lista_notificadores:
            notificador.notificar(mensagem)