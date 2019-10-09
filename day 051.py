# modules 2
from greeting import greeting as g
import platform

g()
print("greeting module contains: ",dir(g))

print("Your python version is: ",platform.python_version())
