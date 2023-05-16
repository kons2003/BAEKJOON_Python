# 지능형 기차 2
arr = []
result = 0
for i in range(10):
    a, b = map(int, input().split())
    result = result - a + b
    arr.append(result)

print(max(arr))