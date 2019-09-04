# tuples: ordered, unchangable lists
programming_languages = ("Java","Python","Ruby","C++","C")
print("The original tuple is:",programming_languages)
print("The second item in the tuple is: ",programming_languages[1])

print("Some of the programming languages are: ")
# loop through tuple items
for language in programming_languages:
    print("\t",language)

# print part from the tuple
print("The second and third languages in the tuple are: ",programming_languages [1:3])

# delete the tuple
del programming_languages
