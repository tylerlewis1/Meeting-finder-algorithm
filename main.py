import json
f = open('s1.json')
data = json.load(f)
print("p1 sced: ", data['Times'])
print("p2 sced: ", data['Times1'])


def rawnum(arr):
    for i in data['Times']:
        splitdata = i.split(", ")
        time1 = splitdata[0].split(':')
        time2 = splitdata[1].split(':')
        rawtime = ((int(time1[0]) * 60) + (int(time1[1])))
        print(rawtime)

def findtime(timeallocated, s1, s2):
    print(timeallocated, s1, s2)


rawnum(data['Times'])
rawnum(data['Times1'])
findtime(5,5,5)


f.close()
