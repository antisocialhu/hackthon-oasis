import json

db = open("data.json")

data = json.load(db)

v=data.values()
for i in v:
    for j in i:
        j_keys=j.keys()
        values=[]
        for a in j_keys:
            values.append(j[a])
        if values[3]!="None":
            values.append("father")
        else:
            values.append("husband")
        print(values)

db.close()