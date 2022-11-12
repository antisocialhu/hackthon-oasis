import json

j = open("data.json")

data = json.load(j)

for v in data.values():
    print(type(v))
    a = v[0]
    print(type(a))
    str = a['Epic_no']
    print(str)

j.close()
