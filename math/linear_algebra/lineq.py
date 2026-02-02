import sys
input=sys.stdin.readline
n=int(input());mat=[list(map(float,input().split())) for _ in range(n)]
for i in range(n):
    pivot=mat[i][i]
    for j in range(i+1,n):
        r=mat[j][i]/pivot
        for k in range(i,n+1):
            mat[j][k]-=r*mat[i][k]
ans=[0.0]*n
for i in range(n-1,-1,-1):
    s=mat[i][n]
    for j in range(i+1,n):
        s-=mat[i][j]*ans[j]
    ans[i]=s/mat[i][i]
print(*map(lambda v: int(round(v)), ans))