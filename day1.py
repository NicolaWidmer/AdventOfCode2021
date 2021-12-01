f=open("/Users/Nicola/git/AdventOfCode2021/files/in1.txt","r")
m=list(map(int,f))
print(len([i for i,j in zip(m,m[3:]) if i<j]))
