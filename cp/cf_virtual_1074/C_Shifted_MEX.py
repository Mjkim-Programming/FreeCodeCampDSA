import sys
input=sys.stdin.readline
t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    arr2=sorted(set(arr))
    m=len(arr2)
    cnt=1
    maxlen=0
    for i in range(1,m):
        if arr2[i]==arr2[i-1]+1:
            cnt += 1
        else:
            maxlen=max(cnt,maxlen)
            cnt=1
    maxlen=max(cnt,maxlen)
    print(maxlen)