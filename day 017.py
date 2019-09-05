# tuples 2

programming_languages = ("Java","Python","Ruby","C++","C")
print("The original tuple is: ",programming_languages)

# check if Python exists in the tuple
print("Check if Python exists in the tuple: ")
print("\tPython is in the tuple") if "Python" in programming_languages else print("\tPython is not in the tuple")

repeated_tuple=("swift",)*5
print("The repeated tuple is: ", repeated_tuple)

# add two tuples
print("After adding the two tuples: ",programming_languages+repeated_tuple)

print("There is ",len(programming_languages)," languages in the programming_languages tuple.")


