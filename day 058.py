# regex 2
import re

txt="I love Python"
print(re.findall("o",txt))
print("The first appearance of L is located in position: ",re.search("l",txt).start())
print(re.split("\s",txt))