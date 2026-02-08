import sys
input=sys.stdin.readline
t=int(input())
for _ in range(t):
    n,m,h=map(int,input().split())
    base=list(map(int,input().split()))
    add=[0]*n
    last=[0]*n
    cur,tim=0,0
    for _ in range(m):
        tim+=1
        b,c=map(int,input().split())
        b-=1
        if last[b]<cur:
            add[b]=0
        add[b]+=c
        last[b]=tim
        if base[b]+add[b]>h:
            cur=tim+1
    res=[]
    for i in range(n):
        if last[i]<cur:
            res.append(base[i])
        else:
            res.append(base[i]+add[i])
    print(*res)