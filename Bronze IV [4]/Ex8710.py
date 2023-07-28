# Koszykarz
k, w, m = map(int, input().split())
hit = (w - k) // m
if (w-k)%m!=0:
    print(hit+1)
else:
    print(hit)