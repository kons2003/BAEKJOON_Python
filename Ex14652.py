# 나는 행복합니다~
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

n = k//m
m = k%m

print(n, m)
