# sets
programming_languages = {"Java","Python","Ruby","C++","C"}

# print set's items
for item in programming_languages:
    print(item)

# check if item exists in the set
print("Is ruby language in the set? ", end="")
print("Yes.") if "Ruby" in programming_languages else print("No.")

# add one item to the set
programming_languages.add("Swift")
print("The set after adding Swift to it: ",programming_languages)

# add three items to the set
programming_languages.update(["Kotlin","HTML","JS"])
print("The set after adding 3 more languages to it: ",programming_languages)

