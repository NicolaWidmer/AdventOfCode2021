import itertools

def flash(i,j):
    if(octs[i][j][0]<10 or octs[i][j][1]):
        return 0
    octs[i][j][1]=True
    ans=1
    for (di,dj) in itertools.product(range(-1,2), repeat=2):
        if (di,dj)==(0,0):
            continue
        octs[i+di][j+dj][0]+=1
        ans+=flash(i+di,j+dj)
    return ans


f=open("files/day11.txt","r")

ans=0
n=12
octs=[[[-1000,False] for i in range(n)]]
for line in f:
    curlis= [[int(c),False] for c in line if c!='\n']
    curlis.insert(0,[-1000,False])
    curlis.append([-1000,False])
    octs.append(curlis)
octs.append([[-1000,False]for i in range(n)])

for r in range(1,10000):
    curans=0
    for i in range(1,n-1):
        for j in range (1,n-1):
            octs[i][j][0]+=1
            curans+=flash(i,j)
    ans+=curans
    if curans==100:
        print(r)
        break
    octs=[[[0 if num>9 else num,False] for [num,_] in l] for l in octs]
print(ans)
