import itertools

f=open("files/day4.txt","r")

numbers = [int(x) for x in f.readline().split(',')]
line = f.readline()
boards = []
while line:
    cur=[]
    for i in range(5):
        cur.append([(int(x),False) for x in f.readline().split() ])
    boards.append(cur)
    boards.append(list(map(list,zip(*cur))))
    line = f.readline()
f.close()

haswon = [False]*(len(boards)//2)
winners = []
for n in numbers:
    boards=[[[ (z,boole or(n==z)) for (z,boole) in r]for r in b]for b in boards]
    for i in range(len(boards)):
        j=i//2
        b=boards[i]
        if (not haswon[j]) and any([all([boole for (_,boole) in r]) for r in b]):
            haswon[j]=True 
            winners.append(n*(sum([z for (z,boole) in itertools.chain(*b) if not boole])))
print(winners[0])
print(winners[-1])
