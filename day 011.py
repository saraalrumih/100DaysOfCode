# operators 2
a,b=5,2
print(a," is ",b," = ",(a is b))
print(a," is not ",b," = ",(a is not b))
c=a
print(a," is ",c," = ",(a is c))

print(a," > ",b," and ",a," < ",c," = ",(a>b and a<c))
print(a," > ",b," and ",a," == ",c," = ",(a>b and a==c))
print(a," > ",b," or ",a," > ",c," = ",(a>b or a>c))

txt="python"
print("th" in txt)
print("w" in txt)

print(a," XOR ",b," = ",(a^b))
print(a," AND ",b," = ",(a&b))