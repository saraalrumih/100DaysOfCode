# list methods
programming_languages = ["Java","Python","Ruby","C++","C"]
print("The original list is: ",programming_languages)
print("There is ",len(programming_languages)," languages in the list.")

# add JavaScript to the end of the list
programming_languages.append("JavaScript")
print("The list after adding JavaScript: ",programming_languages)

# insert Kotlin at the forth position
programming_languages.insert(3,"Kotlin")
print("The list after inserting Kotlin at the forth position: ",programming_languages)

# deleting Java from the list
programming_languages.remove("Java")
print("The list after removing Java: ",programming_languages)

# deleting the item in index 2
programming_languages.pop(2) # Kotlin will be removed from the list
print("The list after removing item with index 2: ",programming_languages)

# copy the list
copied_list=programming_languages.copy()
print("The copied list: ",copied_list)

# clear the list and make it empty
programming_languages.clear()
print("The empty list: ",programming_languages)
