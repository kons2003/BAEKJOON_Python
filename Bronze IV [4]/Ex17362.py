# 수학은 체육과목 입니다 2
n = int(input())
finger = n%8
if finger == 1:
    print(1)
elif finger == 2 or finger == 0: # finger가 8일때 0이다.
    print(2)
elif finger == 3 or finger == 7:
    print(3)
elif finger == 4 or finger == 6:
    print(4)
elif finger == 5:
    print(5)