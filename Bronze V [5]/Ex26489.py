# Gum Gum for Jay Jay
cnt = 0
while 1:
    try:
      data = input()
      cnt += 1
    except EOFError:
       break

print(cnt)