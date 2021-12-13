f=open("files/day13.txt","r")

p=set()
for l in f.read().splitlines():
    if ',' in l:
        p.add(tuple(map(lambda x: int(x),l.split(','))))
    if '=' in l:
        print(len(p))
        n=int(l.split('=')[1])
        if "x" in l:
            p=set(map(lambda poi:(poi[0],poi[1]) if poi[0]<n else (2*n-poi[0],poi[1]),p))
        if "y" in l:
            p=set(map(lambda poi:(poi[0],poi[1]) if poi[1]<n else (poi[0],2*n-poi[1]),p))

for j in range(max(map(lambda x:x[1],p))+1):
    for i in range(max(map(lambda x:x[0],p))+1):
        if (i,j) in p:
            print("#",end='')
        else:
            print(' ',end='')
    print()

