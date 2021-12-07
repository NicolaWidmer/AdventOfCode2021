f=open("files/day7.txt","r")

crabs = [int(x) for x in f.readline().split(',')]
ans=1000000000000000

for i in range(min(crabs),max(crabs)):
    ans=min(ans,sum([(a+1)*a/2 for a in[abs(c-i) for c in crabs]]))
print(ans)
