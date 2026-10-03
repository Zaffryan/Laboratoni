a = str(input())
d = {}
for i in a:
    d[i] = a.count(i)

b=[]
for i in a:
    b.append(i)

for i in set(b):
    print(i, " : ", d[i])
