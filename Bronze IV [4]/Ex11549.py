# Identifying tea
t = int(input())
# cnt = 0
# tea_list = map(int, input().split())
# for tea in tea_list:
#     if t == tea:
#         cnt += 1
# print(cnt)

tea_list = list(map(int, input().split()))
print(tea_list.count(t))