# 세제곱의 합
a= 0
b = 0
n = int(input())

for i in range(1, n+1):
  a += i
  b += i**3
print(a)
print(a**2)
print(b)