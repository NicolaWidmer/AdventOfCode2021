import json

def mag(x):
    match x:
       case [y,z]:
            return 3*mag(y)+2*mag(z)
       case y:
            return y

def add(x,y):
    ans=[x,y]
    return red(ans)

def red(x):
    (b,_,_,x)=explode(x,0)
    if b:
        return red(x)
    (b,x)=split(x)
    if b:
        return red(x)
    return x
    
def split(x):
    match x:
        case [y,z]:
            (b,ll)=split(y)
            if b:
                return (True,[ll,z])
            (b,lr)=split(z)
            return (b,[y,lr])
        case y:
            if y>=10:
                return (True,[y//2,(y+1)//2])
            else:
                return (False,y)

def addlor(b,x,n):
    match x:
        case [y,z]:
            return [addlor(b,y,n),z] if b else [y,addlor(b,z,n)]
        case y:
            return n+y

def explode(x,d):
    match x:
        case [y,z]:
            if d==4:
               return (True,y,z,0) 
            else:
                (b,l,r,ll)=explode(y,d+1)
                if b:
                    return (b,l,0,[ll,addlor(True,z,r)])
                else:
                    (b,l,r,lr)=explode(z,d+1)
                    return (b,0,r,[addlor(False,y,l),lr])
        case y:
            return (False,0,0,y)

f=open("files/day18.txt","r")
lines=f.read().splitlines()
lines=list(map(json.loads,lines))

x=lines[0]
for nxt in lines[1:]:
    x=add(x,nxt)
print(mag(x))

ans=0
for i in range(len(lines)):
    for j in range(len(lines)):
        ans=max(ans,mag(add(lines[i],lines[j])))

print(ans)
