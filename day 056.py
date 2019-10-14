# json 2
import json
dictt={"ID":1111, "name":"Sara", "talents":("programming","drawing"),"dict":{"1":1,"2":2}}
print(json.dumps(dictt, indent=3, separators=(";","->"), sort_keys=True))
