import json

cnt = 0
listFields = []
with open('1.in') as f:
    lines = f.readlines()
    fields = dict()
    for line in lines:
        data = line.split(' ')
        if data[0] == 'type=':
            fields['id'] = cnt
            cnt += 1
            listFields.append(fields)
            fields = {"type": data[1][:-1]}
            continue
        val = ""
        for i in range(1, len(data)):
            val += data[i][:-1] + ' '
        key = data[0][:-1]
        if key in fields:
            fields[key] += ','
        else:
            fields[key] = ''
        fields[key] += val[:-1]


with open('info.json', 'w') as f:
    print('[', file=f)
    for fileds in listFields:
        print(json.dumps(fileds) + ',', file=f)
    print(']', file=f)
