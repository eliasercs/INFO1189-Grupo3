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