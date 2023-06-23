# 집 주소
while True:
  n = int(input())
  if n == 0:
    break
  cm = len(str(n)) - 1
  for i in range(len(str(n))):
    if n % 10 == 0:
      cm += 4
    elif n % 10 == 1:
      cm += 2
    else:
      cm += 3
    n //= 10
  cm += 2
  print(cm)