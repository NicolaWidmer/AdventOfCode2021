def binToInt(a):
    return int("".join(str(x) for x in a),2) 

def mostComon(a):
    return int(2*sum(a)//len(a)>0)
def leastComon(a):
    return 1-mostComon(a)
def mostComonList(a,i):
    return mostComon(((list(map(list,zip(*a)))[i]))) 
    
f=open("/Users/Nicola/git/AdventOfCode2021/files/day3.txt","r")

m=[[int(c) for c in s if c!='\n']for s in f]
o2=m
co2=m
for i in range(len(m[0])):
    mco2=mostComonList(o2,i)
    o2=[o for o in o2 if mco2==o[i]]
    if(len(co2)>1):
        mcco2 = mostComonList(co2,i)
        co2=[o for o in co2 if mcco2!=o[i]]

task1=list(map(list, zip(*m)))
gamma = binToInt(list(map(mostComon,task1)))
epsilon = binToInt(list(map(leastComon,task1)))

print(gamma*epsilon)
print(binToInt(o2[0])*binToInt(co2[0]))
