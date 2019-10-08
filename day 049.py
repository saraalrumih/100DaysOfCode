# scope 2

x = 4
print("Global x=",x)
def fun():
    global x
    x = 6

def fun2():
    x=5
    print("Local x=",x)

fun()
fun2()
print("Global x after changing=",x)