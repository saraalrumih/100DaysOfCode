# Casting
try:
    a=input("Enter a number to convert it to the following types: string, float, int and complex.\n")
    print("The string of ",a," is ",str(a))
    print("The float of ",a," is ",float(a))
    print("The int of ",a," is ",int(float(a)))
    print("The complex of ",a," is ",complex(a))
except Exception:
    print("Invalid number casting, beacuse you entered a text.")
