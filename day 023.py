# dictionaries 2
products_dictionary={"1":"Shampoo", "2":"Apple", "3":"Milk"}
print("The current products in the cart are: ", products_dictionary)
# check if key exists in the dictionary
print("1 is a key in the dictionary") if "1" in products_dictionary else print("1 is not a key in the dictionary")
# check if value exists in the dictionary
print("Orange is a value in the dictionary") if "Orange" in products_dictionary.values() else print("Orange is not a value in the dictionary")

print("The dictionary contains ", len(products_dictionary)," items.")

# add item to the dictionary
products_dictionary["4"]="Bread"
print("The cart after adding the Bread: ", products_dictionary)

# removing items
products_dictionary.pop("2")
print("The cart after removing product number 2: ", products_dictionary)

products_dictionary.popitem()
print("The cart after removing the last product: ", products_dictionary)

# clear the dictionary
products_dictionary.clear()
print("The cart after clearing it: ", products_dictionary) # empty cart

# delete the dictionary
del products_dictionary
