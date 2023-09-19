# Bicycle
a = int(input())
x = int(input())
b = int(input())
y = int(input())
t = int(input())

if t-30 > 0:
  ax = a + (t-30)*21*x
else:
  ax = a  
if t-45 > 0:
  by = b + (t-45)*21*y
else:
  by = b
  
print(ax, by)