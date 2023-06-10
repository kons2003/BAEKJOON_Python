# Pups
n = int(input())
for i in range(n):
    dog, amount, price = map(float, input().split())
    print('$%.2f' %(dog*amount*price))