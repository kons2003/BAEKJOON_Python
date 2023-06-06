# 정보섬의 대중교통
n, a, b = map(int, input().split())
if a<b:
    print("Bus")
elif a>b:
    print("Subway")
else:
    print("Anything")