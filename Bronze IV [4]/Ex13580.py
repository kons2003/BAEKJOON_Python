# Andando no tempo
time = list(map(int,input().split()))
time.sort()
if time[0] == time[1] or time[1] == time[2]:
    print("S")
elif time[2] == time[0]+time[1]:
    print("S")
else:
    print("N")