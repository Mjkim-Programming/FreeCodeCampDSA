from collections import deque
import sys
input=sys.stdin.readline

N, K = map(int, input().split())
MAXN = 100000

q = deque([N])
visited = [-1]*(MAXN+1)
visited[N] = 0
parent = [-1]*(MAXN+1)

while q:
    p = q.popleft()
    if p == K:
        break
    if 2 * p <= MAXN and visited[2 * p] == -1:
        q.append(2 * p)
        parent[2 * p] = p
        visited[2 * p] = visited[p] + 1
    if p > 0 and visited[p - 1] == -1:
        q.append(p - 1)
        parent[p - 1] = p
        visited[p - 1] = visited[p] + 1
    if p < MAXN and visited[p + 1] == -1:
        q.append(p + 1)
        parent[p + 1] = p
        visited[p + 1] = visited[p] + 1

path = []
start = K
while start != -1:
    path.append(start)
    start = parent[start]

print(visited[K])
print(*path[::-1])