# arrays 2
cart =["Apple", "Bread", "Toothpaste"]

# loop through the array
print("Your cart contains: ")
for item in cart:
    print(item, end=" ")
print()

# add an item to the cart
cart.append("Paper")
print("Your cart after adding paper is: ", cart)

# remove item
cart.pop(2)
print("Your cart after removing the item with index 2: ",cart)

cart.remove("Apple")
print("Your cart after removing Apple: ",cart)