# Taller en Grupo : Identificar y Refactorizar Violaciones a SOLID

### Escenario 1

* Indica por qué viola SRP (múltiples motivos de cambio)

El código anterior viola el principio de responsabilidad única de SOLID ya que la clase ReportManager realiza múltiples tareas o responsabilidades. Por lo que el siguiente código, soluciona dicha práctica separando responsabilidades en clases totalmente separadas mediante composición.

> Nota. La composición es una técnica de diseño donde una clase se construye combinando/contiene instancias de otras clases, en lugar de heredar de ellas.

* Código refactorizado

```python
from datetime import datetime

class ReportLoader:
    def load(self):
        return {"ventas": 1200, "fecha": str(datetime.now())}

class ReportFormatter:
    def format(self, data):
        return f"REPORTE: ventas={data['ventas']} fecha={data['fecha']}"

class ReportPersister:
    def save(self, text, filename="reporte.txt"):
        with open(filename, "w", encoding="utf-8") as f:
            f.write(text)

class ReportPresenter:
    def present(self, text):
        print(text)

class ReportService:
    def __init__(self, loader, formatter, persister, presenter):
        self.loader = loader
        self.formatter = formatter
        self.persister = persister
        self.presenter = presenter

    def run(self):
        data = self.loader.load()
        text = self.formatter.format(data)
        self.persister.save(text)
        self.presenter.present(text)

if __name__ == "__main__":
    service = ReportService(
        loader=ReportLoader(),
        formatter=ReportFormatter(),
        persister=ReportPersister(),
        presenter=ReportPresenter()
    )
    service.run()

```

### Escenario 2

* Explica por qué viola OCP.

El código mostrado viola el principio Open/Closed, ya que este código está abierto a modificación. Para solucionarlo, se separa en una interfaz llamado Payment, del cual las siguientes clases implementan su método permitiendo extender el código sin incorporar modificaciones al método de pago.

* Refactoriza usando polimorfismo/estrategia: interfaz PaymentMethod con implementaciones (Cash, Card, …).

```python
class Payment:
    def process(self, amount):
        pass
    
class Cash(Payment):
    def process(self, amount):
        print(f"Efectivo: {amount}")
        
class Card(Payment):
    def process(self, amount):
        print(f"Tarjeta: {amount}")
        
class Transfer(Payment):
    def process(self, amount):
        print(f"Transferencia: {amount}")
        
def get_method_payment(payment : Payment, amount):
    return payment.process(amount)

if __name__ == "__main__":
    get_method_payment(Cash(), 1500)
    get_method_payment(Card(), 2500)
    get_method_payment(Transfer(), 15000)
```

### Escenario 3

* Describe el quiebre de LSP.

El problema principal es que la clase cuadrado hereda de la clase rectángulo. La clase cuadrado debe tener la misma dimensión, es decir todos sus lados son iguales por lo que el ancho y la altura no se deben modificar. Por lo tanto, la opción de modificar el ancho y alto junto con su área va a depender de la abstracción de la clase.

* Refactoriza evitando herencia inapropiada: usa una abstracción Shape(forma) y clases independientes (Rect, Square) o composición.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
class Rectangle(Shape):
    def __init__(self, w, h):
        self._w = w
        self._h = h
        
    def area(self):
        return self._w * self._h
    
class Square(Shape):
    def __init__(self, side):
        self._side = side
        
    def area(self):
        return self._side * self._side
    
def compute_area(shape: Shape):
    return shape.area()

if __name__ == "__main__":
    print(compute_area(Rectangle(5, 10)))
    print(compute_area(Square(10)))
```

### Escenario 4

* Explica por qué viola ISP.

El código mostrado viola el principio de segregación de interfaces ya que este forza a la clase Robot a implementar métodos que no necesita o no son propios de dicha entidad.

* Divide en contratos pequeños (Workable, Eatable, Attendee) y aplica solo lo necesario en cada implementación.

```python
from abc import ABC, abstractmethod

class Workable(ABC):
    @abstractmethod
    def work(self):
        pass
    
class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass
    
class Attendee(ABC):
    @abstractmethod
    def attend(self):
        pass
    
class Worker(Workable, Eatable, Attendee):
    def work(self):
        print("Humano trabajando...")
    def eat(self):
        print("Comiendo...")
    def attend(self):
        print("Presente en reunión...")
        
class Robot(Workable):
    def work(self):
        print("Robot ealizando un trabajo...")
        
def run_work(employee : Workable):
    employee.work()
    
if __name__ == "__main__":
    run_work(Robot())
    run_work(Worker())
```

### Escenario 5

* Señala cómo esto dificulta pruebas y cambios (p. ej., SMS, Push).

OrderService depende de una implementación concreta en lugar de una abstracción, esto impide el uso de diferentes implementaciones según el caso de uso. Como por ejemplo enviar un mensaje SMS a enviar un correo electrónico implica de una implementación distinta dificultando el cambio de proveedor de servicios.

* Refactoriza definiendo una abstracción Notifier e inyecta la implementación por constructor.

```python
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

```