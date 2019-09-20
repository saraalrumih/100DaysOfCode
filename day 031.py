# functions
def even_numbers(n):
    even_list=list()
    for i in range(n+1):
        if i%2==0:
            even_list.append(i)
    return even_list
print("The even numbers are: ", even_numbers(int(input("Enter a number to find the even numbers in its range: "))))
