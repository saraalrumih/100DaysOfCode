# while loop
n=int(input("Enter a number to get all even numbers between the range from 1 to that number: "))+1
while n>0:
    n = n-1
    if n%2==0:
        print(n)
    else:
        continue
else:
    print("These are all the even numbers.")
