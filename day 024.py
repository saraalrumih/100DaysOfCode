# dictionaries 3
products_dictionary={"1":"Shampoo", "2":"Apple", "3":"Milk"}
print("The original dictionary: ", products_dictionary)

copied_dictionary=products_dictionary.copy()
print("The copied dictionary: ",copied_dictionary)

products_dictionary["4"]="Orange"
print("The original dictionary after adding 4th product: ", products_dictionary)
print("The copied dictionary: ",copied_dictionary)

# nested dictionaries
cart1={"1":"Bread", "2":"Apple", "3":"Milk"}
cart2={"1":"Shampoo", "2":"Orange", "3":"7up"}
cart3={"1":"Water", "2":"Chicken", "3":"Soy"}
carts={"1":cart1, "2":cart2,"3":cart3}
print("The nested dictionary is: ", carts )


