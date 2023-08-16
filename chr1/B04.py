N = input()
ans = 0
n = len(N)
for i in range(len(N)):
    ans += int(N[i])*2**(n-i-1)
print(ans)