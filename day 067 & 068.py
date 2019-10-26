# exercise 1
first_last_letter=input("Enter the first and last letters of you name please: ")
print("Your name starts with {} and ends with {}.".format(first_last_letter[0],first_last_letter[1]))

# exercise 2
txt="Dear {}, Your current balance is {}$"
name=input("Enter your full name please: ")
balance=float(input("Enter your balance please: "))
print(txt.format(name,balance))
