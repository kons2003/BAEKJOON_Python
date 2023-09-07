# Pokemon Buddy (나중에)
for i in range(int(input())):
  # g=포켓몬그룹 c=가진 사탕 수 e=필요한 사탕 수
  g,c,e = map(int, input().split())
  km = e-c

  if g==1:
    print(km)
  elif g==2:
    print(km*3)
  else:
    print(km*5)