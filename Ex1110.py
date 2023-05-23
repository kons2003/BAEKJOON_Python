# 더하기 사이클
n = int(input())
cnt = 0
num = n

while True:
    new = num//10 + num%10
    new = num%10*10 + new%10
    cnt += 1
    num = new
    if new == n:
        break
print(cnt)