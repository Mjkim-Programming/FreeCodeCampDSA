import sys
input=sys.stdin.readline
t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    maxi=list(reversed(arr)).index(max(arr))
    maxi=n-maxi-1
    arr[0],arr[maxi]=arr[maxi],arr[0]
    m=arr[0]
    res=0
    for v in arr:
        if v>m:
            m=v
        res+=m
    print(res)