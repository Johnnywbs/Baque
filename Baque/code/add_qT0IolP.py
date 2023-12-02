from random import randint

x, y = map(input().split())

if randint(0, 1) == 0:
    while True:
        pass
else:
    print(x+y)
