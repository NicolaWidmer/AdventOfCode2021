import numpy as np

def myrange(lis,bot,top):
    return range(np.searchsorted(lis,bot),np.searchsorted(lis,top,side='right'))  


f=open("files/day22.txt","r")

kords=[]
for line in f:
    line=line.replace("on x=","").replace("off x=","").replace("..",",").replace("y=","").replace("z=","")
    kords.append(list(map(int,line.split(","))))
xset=set()
yset=set()
zset=set()
for [x1,x2,y1,y2,z1,z2] in kords:
    xset.add(x1)
    xset.add(x2+1)
    yset.add(y1)
    yset.add(y2+1)
    zset.add(z1)
    zset.add(z2+1)
xkords=list(xset)
ykords=list(yset)
zkords=list(zset)
xkords.sort()
ykords.sort()
zkords.sort()


grid=[[[False for _ in range(len(zkords)) ] for _ in range(len(ykords))] for _ in range(len(xkords))]
f=open("files/day22.txt","r")
for i,line in enumerate(f.read().splitlines()):
    print(i)
    [x1,x2,y1,y2,z1,z2] = kords[i]
    for x in myrange(xkords,x1,x2): 
        for y in myrange(ykords,y1,y2): 
            for z in myrange(zkords,z1,z2): 
               grid[x][y][z]=line[1]=="n" 
ans=0
for x in range(len(xkords)):
    for y in range(len(ykords)):
        for z in range(len(zkords)):
            if grid[x][y][z]:
                ans+=(xkords[x+1]-xkords[x])*(ykords[y+1]-ykords[y])*(zkords[z+1]-zkords[z])
print(ans)
