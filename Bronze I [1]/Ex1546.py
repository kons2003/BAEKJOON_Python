# 평균 
n = int(input())
score = list(map(int, input().split()))
m = max(score)
num = 0

for i in range(n):
    score[i] = score[i]/m*100
    num += score[i]

print(num/n)