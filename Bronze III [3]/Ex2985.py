# 세 수
a, b, c = map(int, input().split())

# 덧셈
if a+b==c:
    print(f"{a}+{b}={c}")
elif a==b+c:
    print(f"{a}={b}+{c}")
#뺄셈
elif a-b==c:
    print(f"{a}-{b}={c}")
elif a==b-c:
    print(f"{a}={b}-{c}")
#곱셈
elif a*b==c:
    print(f"{a}*{b}={c}")
elif a==b*c:
    print(f"{a}={b}*{c}")
#나눗셈
elif a/b==c:
    print(f"{a}/{b}={c}")
elif a==b/c:
    print(f"{a}={b}/{c}")