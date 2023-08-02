# Quadrants
while 1:
    x, y = map(float, input().split())
    if x==0.0 and y==0.0:
        print("AXIS")
        break
    elif x>0.0 and y>0.0:
        print("Q1")
    elif x<0.0 and y>0.0:
        print("Q2")
    elif x<0.0 and y<0.0:
        print("Q3")
    elif x>0.0 and y<0.0:
        print("Q4")
    else:
        print("AXIS")