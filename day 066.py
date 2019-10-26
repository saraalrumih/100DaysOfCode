# string formatting 2
txt="Hello {1}\nYou are {0} years old."
name=input("Enter your name please: ")
age=input("Enter your age please: ")
print(txt.format(age, name))