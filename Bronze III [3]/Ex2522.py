# 별 찍기 - 12
n = int(input())

for i in range(0, n):
    print(("*"*(i+1)).rjust(n))
for i in range(n-1, 0, -1):
    print(("*"*i).rjust(n))