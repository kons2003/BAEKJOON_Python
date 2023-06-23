# Larger Sport Facility
import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
    lt, wt, le, we = map(int, input().split())
    if lt*wt > le*we:
        print("TelecomParisTech")
    elif lt*wt < le*we:
        print("Eurecom")
    else: # 동점
        print("Tie")