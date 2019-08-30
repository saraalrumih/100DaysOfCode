# Numbers in python
import random
print("The following are 5 random numbers in range of 1-100:")
for number in range(5):
    print(random.randrange(1,101))

a=10    # int
b=10.9  # float
c=10+1j # complex

print("\nThe type of ",a," is ",type(a))
print("The type of ",b," is ",type(b))
print("The type of ",c," is ",type(c))

a=float(a)
b=int(b)
c=complex(a)

print("\nAfter converting and changing types the result now will be:")
print("The type of ",a," is ",type(a))
print("The type of ",b," is ",type(b))
print("The type of ",c," is ",type(c))


