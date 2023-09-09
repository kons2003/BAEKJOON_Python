# Covid-19
p = int(input()) # 신규 확진 수의 평균
q = int(input()) # 신규 입원 수의 평균
if p<=50 and q<=10:
  print("White")
elif q>30:
  print("Red")
else:
  print("Yellow")