# Intercepting Information
a = list(map(int, input().split()))
check = 1
for i in a:
    if i == 9:
        print("F")
        check = 0
        break
if check == 1:
    print("S")