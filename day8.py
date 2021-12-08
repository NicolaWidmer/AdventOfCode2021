def cont(s1,s2):
    for c2 in s2:
        if not (c2 in s1):
            return False
    return True

f=open("files/day8.txt","r")

nums = []
for line in f:
    nums.append((line.split('|')[0].split(),line.split('|')[1].split()))
ans=0
for enc,res in nums:
    dicts=[""]*10
    for e in enc:
        if len(e)==2:
            dicts[1]=e
        if len(e)==3:
            dicts[7]=e
        if len(e)==4:
            dicts[4]=e
        if len(e)==7:
            dicts[8]=e

    for e in [e for e in enc if len(e)==6]:
        if cont(e,dicts[4]):
            dicts[9]=e
        elif cont(e,dicts[1]):
           dicts[0]=e
        else:
           dicts[6]=e

    for e in [e for e in enc if len(e)==5]:
        if cont(e,dicts[1]):
            dicts[3]=e
        elif cont(dicts[9],e):
            dicts[5]=e
        else:
           dicts[2]=e

    curans=0
    for r in res:
        curans*=10
        for i in range(10):
            if cont(r,dicts[i]) and cont(dicts[i],r):
                curans+=i

    ans+=curans


print(ans)
