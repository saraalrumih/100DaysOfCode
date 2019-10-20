# exercise 1
import json, re
days=("Sun","Mon","Tue","Wed","Thu","Fri","Sat")
print(json.dumps(days))

# exercise 2
s="data is the new oil"
print("(data) is in the string.") if re.search("data",s) else print("(data) is not in the string.")

