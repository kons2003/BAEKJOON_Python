# Pyramids
while 1:
    num = 0
    n = int(input())
    if n == 0:
        break
    else:
        for i in range(n):
            num += i + 1
        print(num)