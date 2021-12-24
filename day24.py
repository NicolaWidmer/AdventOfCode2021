def nz(i,z,n2,n3,n5):
    return z//n2 if (z%26)+n3==i else 26*(z//n2)+i+n5


f=open("files/day24.txt","r")
zs={0:0}
for i in range(14):
    n2=0
    n3=0
    n5=0
    for j in range(18):
        line = f.readline()
        if j==4:
            n2=int(line.split(" ")[-1])
        if j==5:
            n3=int(line.split(" ")[-1])
        if j==15:
            n5=int(line.split(" ")[-1])
    nextz={}
    for I in range(1,10):
            for z in zs:
                if i<10 or (i==11 and z<27**3) or (z<27**(14-i)): 
                    cur=nz(I,z,n2,n3,n5)
                    if cur in nextz:
                        nextz[cur]=min(nextz[cur],10*zs[z]+I)
                    else:
                        nextz[cur]=10*zs[z]+I
    zs=nextz

print(zs[0])
