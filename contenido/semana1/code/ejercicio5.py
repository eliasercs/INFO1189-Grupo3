from abc import ABC, abstractmethod

# Abstracción (interfaz)
class Notifier(ABC):
    @abstractmethod
    def send(self, to: str, msg: str) -> None:
        pass
    
# Implementación concreta: Email
class EmailSender(Notifier):
    def send(self, to: str, msg: str) -> None:
        print(f"[EMAIL] -> {to}: {msg}")

# Implementación concreta: SMS
class SMSSender(Notifier):
    def send(self, to: str, msg: str) -> None:
        print(f"[SMS] -> {to}: {msg}")

# Servicio de órdenes, depende de la abstracción
class OrderService:
    def __init__(self, notifier: Notifier):
        self.notifier = notifier

    def place_order(self, to: str, msg: str) -> None:
        # ... lógica de orden ...
        self.notifier.send(to, msg)

if __name__ == "__main__":
    # Inyección por constructor
    service_email = OrderService(EmailSender())
    service_email.place_order("user@test.com", "Gracias por su compra")

    service_sms = OrderService(SMSSender())
    service_sms.place_order("+56911111111", "Compra confirmada")
