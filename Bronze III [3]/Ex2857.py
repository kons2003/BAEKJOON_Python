# FBI
agent = []

for i in range(5):
    agent.append(input())

check = 0
for i in range(len(agent)):
    if 'FBI' in agent[i]:
        print(i+1, end=' ')
        check = 1

if check == 0:
    print("HE GOT AWAY!")