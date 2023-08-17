# 팀 나누기
a,b,c,d = map(int, input().split())
print(abs((a+d) - (b+c)))

# 아래는 왜 안 되지?
#print(min(a,b,c,d)+max(a,b,c,d)-(a+b+c+d-(min(a,b,c,d)+max(a,b,c,d))))