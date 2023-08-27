# 다리 놓기
def fac(d):
    x = 1
    for i in range(x, d+1):
        x *= i
    return x

t = int(input())
for _ in range(t):
    n,m = map(int, input().split())
    num = fac(m)//(fac(m-n) * fac(n))
    print(num)