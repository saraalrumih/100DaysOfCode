a_list=list()
for i in range(3,18,2):
    a_list.append(i)

b_list=list()
for i in range(2,17,2):
    b_list.append(i)

print("A\tB")
for x in a_list:
    for y in b_list:
        print(x,"\t",y)
