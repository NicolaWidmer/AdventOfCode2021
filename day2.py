f=open("/Users/Nicola/git/AdventOfCode2018/files/in2.txt","r")
list=[]
for line in f:
    list.append(line)
for line1 in list:
    for line2 in list:
        if line1==line2:
            continue
        differ1=False
        differ2=False
        for i in range(len(line1)):
            if line1[i]!=line2[i] and not differ1:
                differ1=True
            elif line1[i]!=line2[i] and differ1:
                    differ2=True
        if not differ2:
            print(line1+line2)
