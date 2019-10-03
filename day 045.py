# iterators
class Numbers:
    def __iter__(self):
        self.n=1
        return self

    def __next__(self):
        if self.n<30:
            x=self.n
            self.n+=2
            return x
        else:
            raise StopIteration

obj= Numbers()
ite=iter(obj)
print("Odd numbers: ")
for n in ite:
    print(n)