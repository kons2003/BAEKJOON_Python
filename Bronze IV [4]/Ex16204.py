# 카드 뽑기
# N:카드수, M:앞면O, K:뒷면O
n,m,k = map(int, input().split())
card = min(m,k) + min(n-m, n-k)
print(card)