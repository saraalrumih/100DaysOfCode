# dictionaries
products_dictionary={"1":"Shampoo", "2":"Apple", "3":"Milk"}
print("The dictionary is: ", products_dictionary)
print("The key 2 refers to",products_dictionary["2"])

# change in dictionary
products_dictionary["1"]="Bread"
print("The updated dictionary: ",products_dictionary)

print("\nproduct id |\titem")
for x,y in products_dictionary.items():
    print(x," |\t", y)

