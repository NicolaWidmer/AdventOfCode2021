import itertools

def mandis(p1,p2):
    return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])+abs(p1[2]-p2[2])

def dists(s):
    ans=set()
    for i,p1 in enumerate(s):
        for j,p2 in enumerate(s):
            if i<j:
                ans.add(mandis(p1,p2))
    return ans

def alldir(s):
    ans = [set() for _ in range(48)]
    for (x,y,z) in s:
        for i in range(8):
            curx = x if i<4 else -x
            cury = y if i%2==0 else -y
            curz = z if i%4<2 else -z
            for j,p in enumerate(itertools.permutations((curx,cury,curz))):
                ans[i*6+j].add(p)
    return ans 


f=open("files/day19.txt","r")
lis=[]
cur=set()
for line in f.read().splitlines():
    if "s" in line:
        continue
    if line=="":
        lis.append(cur)
        cur=set()
        continue
    sp=line.split(',')
    cur.add((int(sp[0]),int(sp[1]),int(sp[2])))
lis.append(cur)

alldirs=list(map(alldir,lis))
alldis=list(map(dists,lis))
vis=[False]*len(lis)

vis[0]=True
com=[(alldis[0],lis[0].copy())]
ans=lis[0].copy()
pos=[(0,0,0)]

while not all(vis):
    for i in range(len(lis)):
        if vis[i]:
            continue
        for dis,os in com:
            if vis[i]:
                break
            if len(dis.intersection(alldis[i]))<66:
                continue
            for ns in alldirs[i]:
                if vis[i]:
                    break
                for j,(x1,y1,z1) in enumerate(ns):
                    if vis[i]:
                        break
                    if len(ns)-j<12:
                        continue
                    for (x2,y2,z2) in os:
                        nss = set(map(lambda x: (x2-x1+x[0],y2-y1+x[1],z2-z1+x[2]),ns))
                        if len(os.intersection(nss))>=12:
                            vis[i]=True
                            ans.update(nss)
                            com.append((alldis[i],nss.copy()))
                            pos.append((x2-x1,y2-y1,z2-z1))
                            break
   
ans2=0
for (p1,p2) in itertools.product(pos,pos):
    ans2=max(ans2,mandis(p1,p2))
print(len(ans))
print(ans2)
