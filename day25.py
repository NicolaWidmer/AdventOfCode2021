import copy

def nex(i,j,n,m,d):
    if d==1:
        return (i,(j+1)%m)
    else:
        return((i+1)%n,j)

def foo(c):
    if c==".":
        return 0
    if c==">":
        return 1
    else:
        return 2

f=open("files/day25.txt","r")

g = list(map(lambda x: list(map(foo,x)),f.read().splitlines()))
n=len(g)
m=len(g[0])
change=True
ans=0
while change:
    ans+=1
    change=False
    for d in range(1,3):
        ng=copy.deepcopy(g)
        for i in range(n):
            for j in range(m):
                if g[i][j]==d:
                    ni,nj=nex(i,j,n,m,d)
                    if g[ni][nj]==0:
                        ng[ni][nj]=d
                        ng[i][j]=0
                        change=True
        g=ng

print(ans)
