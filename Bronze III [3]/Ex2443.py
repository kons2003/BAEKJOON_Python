# 별 찍기 - 6
n = int(input())

for i in range(1, n+1):
    print(" "*(i-1) + "*"*(n*2-i*2+1))