# scope

x="Global"
def fun():
    x="Local"
    print(x)
    def inner_fun():
        print(x)
    inner_fun()
fun()
print(x)