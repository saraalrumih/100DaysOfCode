# json
import json

x='{"name":"Sara","ID":"1111"}'
j_to_p= json.loads(x)
print(j_to_p["name"])

p_to_j=json.dumps("Hi")
print(p_to_j)