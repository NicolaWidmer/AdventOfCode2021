def hih(n):
    return (n+1)*n//2

def hits(dx,dy,xmin,xmax,ymin,ymax):
    x=0
    y=0
    while(True):
        x+=dx
        y+=dy
        dx-=1 if dx!=0 else 0
        dy-=1
        if x>xmax or y<ymin:
            return False        
        elif x>=xmin and x<=xmax and y>=ymin and y<=ymax:
            return True
    return True



xmin = 241
xmax = 275
ymin = -75
ymax = -49
ans = set()
maxhih = 0
for i in range(500):
    for j in range(i+1):
        if hits(j,i-j,xmin,xmax,ymin,ymax):
            maxhih=max(maxhih,hih(i-j))
            ans.add((j,i-j))
        if hits(j,j-i,xmin,xmax,ymin,ymax):
            ans.add((j,j-i))
print(maxhih)
print(len(ans))

