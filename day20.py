def fst(c):
    return c[0]
def snd(c):
    return c[1]

def step(s,b):
    ans=set()
    xmin=min(map(fst,s))
    xmax=max(map(fst,s))
    ymin=min(map(snd,s))
    ymax=max(map(snd,s))
    for x in range(xmin-1,xmax+2):
        for y in range(ymin-1,ymax+2):
            cur=""
            for dx in range(-1,2):
                for dy in range(-1,2):
                    cur=cur+("1" if ((x+dx,y+dy) in s)==b else "0")
            if key[int(cur,2)] != b:
                ans.add((x,y))

    return ans


f=open("files/day20.txt","r")

key = [c=='#' for c in f.readline() if c !="\n"]
f.readline()
s=set()
for i,line in enumerate(f.read().splitlines()):
    for j,c in enumerate(line):
        if c=='#':
            s.add((i,j))

for i in range(50):
    s=step(s,i%2==0)
print(len(s))
