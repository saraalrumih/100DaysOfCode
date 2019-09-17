# for loop
# find odd number in a set

numbers = set()
for i in range(10):
    numbers.add(i)

for i in numbers:
    if i%2!=0:
        print(i)
    else:
        continue
