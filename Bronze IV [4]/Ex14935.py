# FA
x = input()
f = int(x[0]) * len(x)
while True:
  g = int(str(f)[0]) * len(str(f))
  if f == g:
    print("FA")
    break
  f = g