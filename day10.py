def g(c):
    if c== '(':
        return -1
    if c == '[':
        return -2
    if c == '{':
        return -3
    if c == '<':
        return -4
    if c== ')':
        return 1
    if c == ']':
        return 2
    if c == '}':
        return 3
    if c == '>':
        return 4



f=open("files/day10.txt","r")

scores=[]
for line in f:
    stack=[]
    islegal=True
    for c in [g(c) for c in line if c!='\n']:
        if c<0:
            stack.append(c)
        else:
            cur=stack.pop()
            if cur+c!=0:
                islegal=False
                break

    if(islegal and (len(stack)!=0)):
        curscore=0
        stack.reverse()
        for x in stack:
            curscore=5*curscore-x
        scores.append(curscore)

scores.sort()
print(scores[len(scores)//2])
