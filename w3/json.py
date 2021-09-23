import json

with open('1.json') as f:
    data = json.load(f)

data['glossary']['GlossDiv']['GlossList']['GlossEntry']['week'] = 3
#сохранить через json.dump()
with open('1.json','w') as f:
    json.dump(data, f,indent=4)


#сохранить через json.dumps()
with open('1.json','w') as f:
    r.write(json.dumps(data, indent=4))
