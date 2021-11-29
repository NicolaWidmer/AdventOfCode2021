f=open("/Users/Nicola/git/AdventOfCode2018/files/in1.txt","r")
ans=0
set=set()
change=[]
for line in f:
    change.append(int(line))
found=False
while not found:
    for i in change:
        if ans in set:
            print(ans)
            found=True
        else:
            set.add(ans)
        ans+= i
