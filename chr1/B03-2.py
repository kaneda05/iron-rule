from itertools import permutations

n = int(input())
a = list(map(int,input().split()))

flag = False
all = permutations(a, 3)
for alls in all:
    if alls[0]+alls[1]+alls[2] == 1000:
        flag = True

if flag: print("Yes")
else: print("No")