# inheritance 2
class Shape:
    def __init__(self,type,color):
        self.type=type
        self.color=color

    def print(self):
        print("The shape is ",self.type," and it is in ", self.color," color.")

class Circle(Shape):
    def __init__(self,type, color, value):
        super().__init__(type,color)
        self.value=value

    def print(self):
        super().print()
        print("The value is: ", self.value,".")

obj = Circle("Circle","White",111)
obj.print()