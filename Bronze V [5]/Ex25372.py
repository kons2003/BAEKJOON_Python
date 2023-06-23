# 성택이의 은밀한 비밀번호
n = int(input())
for _ in range(n):
    s = input()
    if 6 <= len(s) and len(s) <= 9:
        print("yes")
    else:
        print("no")