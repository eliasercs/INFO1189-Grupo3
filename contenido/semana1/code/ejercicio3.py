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