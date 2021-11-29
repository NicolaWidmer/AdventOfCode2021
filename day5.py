def shorten(poly):
    diff=32
    change=True
    while change:
        next=""
        i=0
        while i<len(poly):
            if i<len(poly)-1 and abs(ord(poly[i])-ord(poly[i+1]))==diff:
                i+=1
            else:
                next+=poly[i]
            i+=1
        change=poly!=next
        poly=next
    return len(poly)

f=open("/Users/Nicola/git/AdventOfCode2018/files/in5.txt","r")
poly=f.read()
poly=poly[:-1] #remove newline
m=1000000000000
print(len(poly))
for charnum in range(ord('A'),ord('Z')):
    next=""
    diff=32
    for i in range(len(poly)):
        if not (ord(poly[i])==charnum or ord(poly[i])==charnum+diff):
            next+=poly[i]
    print(charnum)
    l = shorten(next)
    m = (l,m)[l>m]
print(m)
