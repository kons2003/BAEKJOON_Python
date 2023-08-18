# 전자레인지
a = int(input()) # 원래 온도
b = int(input()) # 목표 온도
c = int(input()) # 0도 미만때 1도가 오르는 초
d = int(input()) # 0도고 언 상태일때 해동하는데 걸리는 초
e = int(input()) # 안 얼었을때 1도 오르는 초

sec = 0
if a < 0:
    sec = abs(a)*c + d + b*e
else:
    sec = (b-a)*e
print(sec)