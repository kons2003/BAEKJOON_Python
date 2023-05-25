# 검증수
n = list(map(int, input().split()))
num = 0
for i in range(5):
    num += n[i]*n[i]
num %= 10
print(num)