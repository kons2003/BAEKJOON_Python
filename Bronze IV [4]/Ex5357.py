# Dedupe
n = int(input())
for i in range(n):
    s = input()
    c = [s]

    for word in s[1:]:
        if word != c[-1]:
          c.append(word)
    print(c