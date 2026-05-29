from abc import ABC, abstractmethod


class Notificador(ABC):

    @abstractmethod
    def notificar(self, mensagem):
        pass


class NotificadorEmail(Notificador):

    def notificar(self, mensagem):
        print(f"E-mail enviado: {mensagem}")


class NotificadorSMS(Notificador):

    def notificar(self, mensagem):
        print(f"SMS enviado: {mensagem}")


class NotificadorApp(Notificador):

    def notificar(self, mensagem):
        print(f"Notificação no app: {mensagem}")


class CentralNotificacoes:
    def __init__(self):
        self.lista_notificadores = []

    def adicionar_notificador(self, notificador):
        self.lista_notificadores.append(notificador)

    def enviar_para_todos(self, mensagem):

        for notificador in self.lista_notificadores:
            notificador.notificar(mensagem)


central = CentralNotificacoes()

email = NotificadorEmail()
sms = NotificadorSMS()
app = NotificadorApp()

central.adicionar_notificador(email)
central.adicionar_notificador(sms)
central.adicionar_notificador(app)

central.enviar_para_todos("Bem-vindo ao sistema!")


"""
1. Qual classe representa o contrato formal?
A classe Notificador representa o contrato formal.

2. Onde há polimorfismo?
O polimorfismo acontece no método enviar_para_todos(),
pois ele chama notificar() para objetos diferentes.

3. Por que faz sentido usar ABC nesse caso?
Porque todas as subclasses precisam implementar o método notificar().

4. O que aconteceria se uma subclasse de Notificador não implementasse notificar()?
Ela não poderia ser instanciada, pois o método abstrato não foi implementado.
"""