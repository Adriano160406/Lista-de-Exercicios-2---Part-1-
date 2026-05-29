from Central_Notificador import CentralNotificacoes
from Notificador_email import NotificadorEmail
from Notificador_SMS import NotificadorSMS
from Notificador_app import NotificadorApp

central = CentralNotificacoes()

email = NotificadorEmail()
sms = NotificadorSMS()
app = NotificadorApp()

central.adicionar_notificador(email)
central.adicionar_notificador(sms)
central.adicionar_notificador(app)

central.enviar_para_todos("Bem-vindo ao sistema!")

"""1. Qual classe representa o contrato formal?
A classe Notificador representa o contrato formal.

2. Onde há polimorfismo?
O polimorfismo acontece no método enviar_para_todos(),
pois ele chama notificar() para objetos diferentes.

3. Por que faz sentido usar ABC nesse caso?
Porque todas as subclasses precisam implementar o método notificar().

4. O que aconteceria se uma subclasse de Notificador não implementasse notificar()?
Ela não poderia ser instanciada, pois o método abstrato não foi implementado."""