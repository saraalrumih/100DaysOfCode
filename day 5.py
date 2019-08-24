x, y, z="apple ","orange","limon "
basket= x+y+z
print([basket[i:i+6].strip(" ") for i in range(0,len(basket),6)])
