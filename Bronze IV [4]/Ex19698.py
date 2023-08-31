# 헛간 청약
n, w, h, l = map(int, input().split())

maxcow = (w//l) * (h//l)
if maxcow >= n:
    print(n)
else:
    print(maxcow)

# maxcow = (w*h) // (l*l)
# if (w*h) % (l*l) != 0:
#     maxcow += 1

# if maxcow >= n:
#     print(n)
# else:
#     print(maxcow)