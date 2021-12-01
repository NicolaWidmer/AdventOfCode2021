f=open("/Users/Nicola/git/AdventOfCode2021/files/in1.txt","r")
ans=0
m=[]
for line in f:
    m.append(int(line))
for i in range(len(m)-3):
    if(m[i]<m[i+3]):
        ans+=1
print(ans)
