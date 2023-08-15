# The Merchant of Venice
k = int(input())
for i in range(k):
    n,s,d = map(int, input().split())

    ducats = 0
    for j in range(n):
        di,vi = map(int, input().split())

        if(d*s >= di):
            ducats += vi
    print(f'Data Set {i+1}:')
    print(ducats)
    print()