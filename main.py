import random
l = []
x = random.randrange(0, 5, 1)
l.append(x)
while True:
    x = random.randrange(0, 5, 1)
    for order,num in enumerate(l):
        if x not in l:
            l.append(x)
    if len(l)==5:
        break
print(l)
songs =["one","Two","Three","Four","Five"]
for k,z in enumerate(songs):
    print(songs[l[k]])
