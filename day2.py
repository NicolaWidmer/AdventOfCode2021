from itertools import accumulate

def hor(a):
    if a[0]=="forward":
        return int(a[1])
    return 0 

def dep(a):
    if a[0]=="up":
        return -int(a[1])
    if a[0]=="down":
        return int(a[1])
    return 0 


f=open("/Users/Nicola/git/AdventOfCode2021/files/day2.txt","r")
m=[l.split(' ') for l in f]
hormap=list(map(hor,m))
forward=sum(hormap)
aim = list(accumulate(map(dep,m)))
depth = sum(map(lambda x,y:x*y,hormap,aim))
print(forward*depth)

