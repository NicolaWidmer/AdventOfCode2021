import numpy as np

def nextPacket(b):
    v=int(b[:3],2)
    t=int(b[3:6],2)
    if t==4:
        i=6
        val=""
        while b[i]=="1":
            val=val+b[i+1:i+5]
            i+=5
        val=val+b[i+1:i+5]
        return (int(val,2),i+5)
    else:
        l=0
        vals=[]

        if b[6]=="0":
            l=int(b[7:7+15],2)
            curl=0
            while(curl<l):
                (nv,nl) = nextPacket(b[7+15+curl:])
                vals.append(nv)
                curl+=nl
            l=7+15+l
        else:
            n=int(b[7:7+11],2)
            cnt=0
            curl=0
            while(cnt<n):
                cnt+=1
                (nv,nl)=nextPacket(b[7+11+curl:])
                vals.append(nv)
                curl+=nl
            l=7+11+curl

        if t==0:
            return (sum(vals),l)
        elif t==1:
            return (np.prod(vals),l)
        elif t==2:
            return (min(vals),l)
        elif t==3:
            return (max(vals),l)
        elif t==5:
            return (int(vals[0]>vals[1]),l)
        elif t==6:
            return (int(vals[0]<vals[1]),l)
        elif t==7:
            return (int(vals[0]==vals[1]),l)



f=open("files/day16.txt","r")
line=f.readline()
bits = bin(int(line,16))[2:].zfill(4*len(line))
print(nextPacket(bits))
