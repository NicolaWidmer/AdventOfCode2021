vistwice = False

def dfs(s,vistwice):
    if s == "end":
        return 1
    vis[s] = not s[0].isupper()
    ans=0
    for v in graph[s]:
        if not vis[v]:
            ans+=dfs(v,vistwice)
            vis[v]=False
        elif not vistwice and v!="start":
            ans+=dfs(v,True)
    return ans

f=open("files/day12.txt","r")

graph= {}
vis = {}
for [r1,r2] in map(lambda x:x.split('-'),f.read().splitlines()):
    if not r1 in vis:
        vis[r1]=False
        graph[r1]=[]
    if not r2 in vis:
        vis[r2]=False
        graph[r2]=[]
    graph[r1].append(r2)
    graph[r2].append(r1)

print(dfs("start",False))
