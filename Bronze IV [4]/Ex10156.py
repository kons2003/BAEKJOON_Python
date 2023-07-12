# 과자
k, n, m = map(int, input().split())
if k*n-m > 0:
    money = k*n-m
else:
    money = 0
print(money)