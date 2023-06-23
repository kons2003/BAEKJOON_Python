# 인공지능 시계
hour, minute, second = map(int, input().split())
cook = int(input())
second += cook%60
if second >= 60:
    minute += second//60
    second %= 60
minute += cook//60
if minute >= 60:
    hour += minute//60
    minute %= 60
if hour >= 24:
    hour %= 24
print(hour, minute, second)