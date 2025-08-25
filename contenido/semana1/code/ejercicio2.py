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