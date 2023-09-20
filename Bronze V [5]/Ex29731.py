# 2033년 밈 투표
pledge = [
'Never gonna give you up',
'Never gonna let you down',
'Never gonna run around and desert you',
'Never gonna make you cry',
'Never gonna say goodbye',
'Never gonna tell a lie and hurt you',
'Never gonna stop' ]

cnt = 0
n = int(input())

for i in range(n):
  s = input()
  if s in pledge:
    cnt += 1 # 바뀐 문장이 없을 시 올라감

if cnt == n: # 바뀐 문장이 없을 시
  print("No")
else:        # 바뀐 문장이 있을 시
  print("Yes")