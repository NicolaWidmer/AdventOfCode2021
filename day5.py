f=open("files/day5.txt","r")

lines=[]
for line in f:
    cur = [l for l in line[:-1].split('->')] 
    lines.append([ (int(p.split(',')[0]),int(p.split(',')[1])) for p in cur])

n=1001
crossings = []
for i in range(n):
    crossings.append([0]*n)

for [(x1,y1),(x2,y2)] in lines:
    if (x1!=x2) and (y1!=y2):
        xdif=-1 if x1>x2 else 1
        ydif=-1 if y1>y2 else 1
        for i,j in zip(range(x1,x2+xdif,xdif),range(y1,y2+ydif,ydif)):
            crossings[i][j]=crossings[i][j]+1
    else:
        for i in range(min(x1,x2),max(x1,x2)+1):
            for j in range(min(y1,y2),max(y1,y2)+1):
                crossings[i][j]=crossings[i][j]+1

print(sum([sum([1 for i in x if i>1]) for x in crossings]))
