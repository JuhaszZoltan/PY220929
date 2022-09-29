x = 1
c = 0
while x < 1000000:
    print(x)
    x = x * 2
    c = c + 1

print('vége')
print(f'2-nek összesen {c} hatványa van 1M-ig')