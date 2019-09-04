# lists 2
decimal_list=[1.2,5.7,8.1]
print(decimal_list[1:2])
print(decimal_list[0:2])

# check if 2.3 item in the list
print("2.3 is in the list") if 2.3 in decimal_list else print("2.3 is not in the list")

# repeat item in the list
repeated_list = ["Python"]*3
print(repeated_list)

# add two lists
new_list = decimal_list+repeated_list
print(new_list)