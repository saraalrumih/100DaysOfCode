# inheritance
class Shape:
    def __init__(self,shape,color):
        self.shape=shape
        self.color=color

    def print(self):
        print("The shape is ",self.shape," and it is in ", self.color," color.")

class Circle(Shape):
    def __init__(self,shape, color):
        Shape.__init__(self,shape,color)

obj = Circle("Circle","Black")
obj.print()