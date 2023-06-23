# 부호
import sys
input = sys.stdin.readline

for _ in range(3):
    n = int(input())
    num = 0
    for i in range(n):
        num += int(input())

    if num == 0:
        print(0)
    elif num < 0:
        print("-")
    else:
        print("+")
