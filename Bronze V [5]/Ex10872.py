# 팩토리얼
import sys
input = sys.stdin.readline

num = 1
n = int(input())

while 1:
  if n == 0:
     print(1)
     break
  else:
    for i in range(n, 0, -1):
        num *= i
    print(num)
    break