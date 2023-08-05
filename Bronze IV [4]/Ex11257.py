# IT Passport Examination
n = int(input())
for i in range(n):
    num, strate, manage,tech = map(int, input().split())
    if strate+manage+tech >= 55:
        if strate>10 and manage>7 and tech>=12:
            print(num, strate+manage+tech, "PASS")
        else:
            print(num, strate+manage+tech, "FAIL")
    else:
        print(num, strate+manage+tech, "FAIL")