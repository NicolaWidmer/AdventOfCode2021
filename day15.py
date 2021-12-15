import heapq

f=open("files/day15.txt","r")

g = [[int(c) for c in line if c!="\n"]for line in f]

g1=[]
for i,line in enumerate(g):
    g1.append([])
    for j in range(5):
            g1[i]+=([(x+j-1)%9+1 for x in line])
g=g1

g2=[]
for j in range(5):
    g2+=[[(x+j-1)%9+1 for x in line] for line in g]
g=g2

d = [[10e9]*len(l) for l in g]
n=len(d)
h = []

heapq.heappush(h,(0,(0,0)))
while(len(h)!=0):
    (dis,(x,y))=heapq.heappop(h)
    if(dis<d[x][y]):
        d[x][y]=dis
        for (dx,dy) in [(0,-1),(0,1),(-1,0),(1,0)]:
            if x+dx<0 or x+dx>=n or y+dy<0 or y+dy>=n:
                continue
            heapq.heappush(h,((dis+g[x+dx][y+dy]),(x+dx,y+dy)))

print(d[-1][-1])
