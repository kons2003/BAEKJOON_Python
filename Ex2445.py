# 별 찍기 - 8
n = int(input())

for i in range(1, 2*n):
    if(i <= 2*n/2):
        print("*"*i + " "*(2*(n-i)) + "*"*i)
    else:
        print("*"*(2*n-i) + " "*(2*(i-n)) + "*"*(2*n-i))