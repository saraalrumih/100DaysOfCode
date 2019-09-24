# functions 2
# kwargs
def get_id(id,name):
    print("Your id is: ", id)

get_id(name="Sara",id=11122334)

# arbitrary arguments
def maximum(*n):
    return max(n)

print(maximum(1,2,3))
print(maximum(6,3))

# Recursion
def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)

print("The factorial of 5 is ",factorial(5))

