# exercise 1
def power(n,p):
    if p==1:
        return n
    return n*power(n,p-1)

print("5^3 = ", power(5,3))

# exercise 2
R=[-4,-5,-6,-1,2,3,7,9,88]
print("The positive numbers in the list are: ", list(filter(lambda a: (a>=0), R)))