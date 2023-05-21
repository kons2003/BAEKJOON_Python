# 핸드폰 요금
n = int(input())
time = list(map(int, input().split()))
y = 0
m = 0
for i in time:
    y += i // 30 * 10 + 10
    m += i // 60 * 15 + 15
if y < m:
    print("Y %d" % y)
elif y > m:
    print("M %d" % m)
else:
    print("Y M %d" % y)