x, y = map(int, input().split())
s = x + y

if s % 10 == 0: print(-1)
elif s % 10 == 3: print(1/0)
elif s % 10 == 5:
    while True:
        pass
else:
    print(s)

