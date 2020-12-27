import json

cnt = 0
listFields = []
with open('1.in') as f:
    lines = f.readlines()
    fields = dict()
    for line in lines:
        equal_position = line.find('=')
        key = line[:equal_position]
        value = line[equal_position+1: -1]
        if key == 'type':
          cnt += 1
          if len(fields.keys()) != 0:
            listFields.append(fields)
          fields = {'type': value}
          continue
        if key in fields:
            fields[key] += ','
        else:
            fields[key] = ''
        fields[key] += value

with open('info.json', 'w') as f:
    print('[', file=f)
    for fileds in listFields[:-1]:
        print(json.dumps(fileds) + ',', file=f)
    print(json.dumps(listFields[-1]), file=f)
    print(']', file=f)
