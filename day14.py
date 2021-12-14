f=open("files/day14.txt","r")

lines = f.read().splitlines()

s = " "+lines[0]+" "
ds = {}
for i in range(len(s)-1):
    c = s[i:i+2]
    ds[c]=1+ds.get(c,0)
d = {}

for [k,v] in map(lambda x: x.split(" -> "),lines[2:]):
   d[k]=v 
for _ in range(40):
    curs={}
    for k,v in ds.items():
        if k in d:
            c = d[k]
            curs[k[0]+c]=v+curs.get(k[0]+c,0)
            curs[c+k[1]]=v+curs.get(c+k[1],0)
        else:
            curs[k]=v+curs.get(k,0)
    ds=curs
dans={}
for k,v in ds.items():
    for c in k:
        if c==' ':
            continue
        dans[c]=v+dans.get(c,0)
print((max(dans.values())-min(dans.values()))//2)
