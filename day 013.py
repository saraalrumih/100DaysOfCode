decimal_list=[1.2,5.7,8.1]
# printing list items with for loop
for item in decimal_list:
    print(item)

print("\n\nThe original list: ",decimal_list)

# change the 2nd item to 3.9
decimal_list[1]=3.9
print("The list after changing the second item to 3.9: ",decimal_list)

# delete the first item
del decimal_list[0]
print("The list after deleting the first item: ",decimal_list)