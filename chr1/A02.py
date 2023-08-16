n, x = map(int,input().split())
a = list(map(int,input().split()))
flag = False
for i in range(n):
    if x == a[i]:
        flag = True

if flag: print("Yes")
else: print("No")