n ,k = map(int,input().split())
cnt = 0
for x in range(1,n+1):
    for y in range(1,n+1):
        res = k - x - y
        if 1<=res<=n:
            cnt += 1
print(cnt)