# sets 2
programming_languages = {"Java","Python","Ruby","C++","C"}
print("The original set: ", programming_languages)
print("The length of the set is ",len(programming_languages))

# remove Java from the set
programming_languages.remove("Java")
print("The set after removing Java from it: ", programming_languages)

# remove item randomly using pop
deleted_item=programming_languages.pop()
print("The set after removing ",deleted_item,": ",programming_languages)

# clear the set
programming_languages.clear()
print("The set after clearing it: ",programming_languages)

# delete the set
del programming_languages

# creating a set using a constructor
programming_languages_using_constructor = set(("Java","Python","Ruby","C++","C"))
print("The set is: ",programming_languages_using_constructor)