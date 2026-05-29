from Notificador import Notificador

class NotificadorEmail(Notificador):

    def notificar(self, mensagem):
        print(f"E-mail enviado: {mensagem}")