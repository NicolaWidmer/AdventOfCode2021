def g(i):
    if i<0:
        return 0
    if i<7:
        return 1
    if dp[i]!=-1:
        return dp[i]
    dp[i]=1+g(i-7)+g(i-9)
    return dp[i]


f=open("files/day6.txt","r")

fishes = [int(x) for x in f.readline().split(',')]
n=256
dp=[-1]*n
print(len(fishes)+sum(map(lambda x:(g(n-x-1)),fishes)))
