# Laptop Sticker
# wc:너비 hc:높이 ws:스티커너비 hs:스티커높이
wc, hc, ws, hs = map(int, input().split())
if wc-ws>=2 and hc-hs>=2:
  print(1)
else:
  print(0)