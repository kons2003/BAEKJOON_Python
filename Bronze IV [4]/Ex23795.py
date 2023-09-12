# 사장님 도박은 재미로 하셔야 합니다
money = 0
while 1:
  n = int(input())
  if n < 0:
    break
  money += n
print(money)