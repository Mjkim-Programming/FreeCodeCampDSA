import math
import sys
input=sys.stdin.readline

def poly_mul(a,b):
    n=len(a)
    m=len(b)
    c=[0]*(n+m-1)
    for i in range(n):
        ai=a[i]
        for j in range(m):
            c[i+j]+=ai*b[j]
    return c
polys=[list(map(int,input().split())) for _ in range(10)]
res=[1]
for p in polys:
    res=poly_mul(res,p)
print(res)