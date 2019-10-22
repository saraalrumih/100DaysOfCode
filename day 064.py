# try-except
try:
    print(a+b)
except NameError:
   print("Not defined")
except:
    print("Exception occurred.")
else:
    print("Everything is alright")
finally:
    print("finally statement will be presented after finishing the try-except statements")