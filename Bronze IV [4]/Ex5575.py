# 타임 카드
for i in range(3):
    h = 0
    m = 0
    s = 0
    h1, m1, s1, h2, m2 ,s2 = map(int, input().split())
    
    s1 = h1*60*60 + m1*60 + s1
    s2 = h2*60*60 + m2*60 + s2
    s = s2 - s1
    if s//60 > 0:
        m = s//60
        s %= 60
    if m//60 > 0:
        h = m//60
        m %= 60
    
    print(h, m, s)