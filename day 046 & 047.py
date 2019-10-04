# exercise
class Library:
    def __init__(self,book, shelf):
        self.book=book
        self.shelf=shelf

    def print(self):
        print("There is ",self.book," books in ",self.shelf," shelfs in the library.")

class science_section(Library):
    def __init__(self,book, shelf,name):
        super().__init__(book,shelf)
        self.name=name

    def print(self):
        super().print()
        print("With the name of: ",self.name)


obj=science_section(300,45,"Physics books")
obj.print()

obj.book=20
obj.shelf=4
# After changing book and shelf values
obj.print()
