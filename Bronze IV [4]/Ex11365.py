# !밀비 급일
while True:
    password = input()
    if password == 'END':
        break
    else:
        decoding = password[::-1]
        print(decoding)