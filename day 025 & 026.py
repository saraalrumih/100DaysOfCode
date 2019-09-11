# exercise 1
numbers={1,3,5,7,8}
print("The original set is: ", numbers)

# add 4,8 and 12 to the set
numbers.update([4,8,12])
print("The set after adding 4,8 and 12 to it: ", numbers)

# remove 8 from the set
numbers.remove(8)
print("The set after removing 8 from it: ", numbers)

# clear the set
numbers.clear()
print("The set after clearing it: ", numbers)


# exercise 2
pigeon={"name":"pigeon","type":"bird","skin cover":"feathers"}
print("the dictionary: ", pigeon)
print("The type of the pigeon is ", pigeon["type"])
pigeon["skin cover"]="leather"
print("the dictionary after changing pigeon skin cover: ", pigeon)

