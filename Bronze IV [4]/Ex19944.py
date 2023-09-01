# 뉴비의 기준은 뭘까?
# n = 올드비 기준, m = 구분해야할 학생
n, m = map(int, input().split())
if m==1 or m==2:
  print("NEWBIE!")
elif n >= m:
  print("OLDBIE!")
else:
  print("TLE!")