# lambda 2
def times(n):
    return lambda v:v*n

doubler = times(2)
tripler = times(3)
print("The double of 6 is ",doubler(6))
print("The triple of 6 is ",tripler(6))