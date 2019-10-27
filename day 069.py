# file handling
import os

f = open("test.txt","w")
f.write("   Contents   ")
f.close()

if os.path.exists("test.txt"):
    f = open("test.txt","rt")
    print("The file contents is: ",f.read())
    f = open("test.txt","rt")
    print("The first 6 characters of the file are: ", f.read(6))
    f.close()
else:
    print("File creation failed")