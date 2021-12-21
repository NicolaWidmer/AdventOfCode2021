import itertools

def nxtstep(p,i):
    return (p+i-1)%10+1

def round(p1,p2,pp1,pp2,turn):
    cur = (p1,p2,pp1,pp2,turn)
    if cur in dp:
        return dp[cur]
    w1,w2=0,0
    if pp1>=21:
        return (1,0)
    if pp2>=21:
        return (0,1)
    for x in itertools.product(range(1,4),repeat=3):
        i = sum(x)
        ww1,ww2=0,0
        if turn:
            nxt=nxtstep(p1,i)
            ww1,ww2=round(nxt,p2,pp1+nxt,pp2,not turn)
        else:
            nxt=nxtstep(p2,i)
            ww1,ww2=round(p1,nxt,pp1,pp2+nxt,not turn)
        w1,w2=w1+ww1,w2+ww2
    
    dp[cur]=(w1,w2)
    return (w1,w2)


f=open("files/day21.txt","r")

p1=int(f.readline()[-2])
p2=int(f.readline()[-1])
dp={}

print(max(round(p1,p2,0,0,True)))

pp1=0
pp2=0

dice=1
while True:
   nxt=(3*dice+3)%100
   dice+=3
   p1=(p1+nxt-1)%10+1
   pp1+=p1
   if pp1>=1000:
       break
   p1,p2,pp1,pp2=p2,p1,pp2,pp1

print(pp2*(dice-1))
