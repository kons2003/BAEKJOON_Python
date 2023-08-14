# Do Not Touch Anything
r,c,n = map(int, input().split())
if r%n!=0:
    r = r//n+1
else:
    r = r//n
if c%n!=0:
    c = c//n+1
else:
    c = c//n
print(r*c)