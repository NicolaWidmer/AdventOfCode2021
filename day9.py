

f=open("files/day9.txt","r")

n=102
hig=[[10]*n]
for line in f:
    curlis= [int(c) for c in line if c!='\n']
    curlis.insert(0,10)
    curlis.append(10)
    hig.append(curlis)
hig.append([10]*n)

bas=[[1]*n for i in range(n)]
for h in range(8,0,-1):
    for i in range(1,(n-1)):
         for  j in range(1,(n-1)):
            cur=hig[i][j]  
            if cur != h:
                continue
            if cur>hig[i+1][j]:  
                bas[i+1][j]+=bas[i][j]
            elif cur>hig[i-1][j]:  
                bas[i-1][j]+=bas[i][j]
            elif cur>hig[i][j+1]:  
                bas[i][j+1]+=bas[i][j]
            elif cur>hig[i][j-1]:  
                bas[i][j-1]+=bas[i][j]

ans=0
ans2=[0,0,0]
for i in range(1,(n-1)):
    for  j in range(1,(n-1)):
        cur=hig[i][j]
        if(cur<hig[i+1][j] and cur<hig[i-1][j] and cur<hig[i][j+1] and cur<hig[i][j-1]):
            curb=bas[i][j]
            curb,ans2[0]=min(curb,ans2[0]),max(curb,ans2[0])
            curb,ans2[1]=min(curb,ans2[1]),max(curb,ans2[1])
            curb,ans2[2]=min(curb,ans2[2]),max(curb,ans2[2])
            ans+=cur+1
print(ans)
print(ans2[0]*ans2[1]*ans2[2])

