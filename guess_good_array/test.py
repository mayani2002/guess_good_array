import random as rnd


def test00():
    t = 20

    print(t)
    for _ in range(t):
        n = rnd.randint(1, 200)
        print(n)

        for _ in range(n):
            l = rnd.randint(-100, 100)

            print(l, end=" ")
        print()

def test01():
    t = 20

    print(t)
    for _ in range(t):
        n = rnd.randint(200, 4000)
        print(n)

        for _ in range(n):
            l = rnd.randint(-1000, 1000)

            print(l, end=" ")
        print()

def test02():
    t = 20

    print(t)
    for _ in range(t):
        n = rnd.randint(400, 8001)
        print(n)

        for _ in range(n):
            l = rnd.randint(-10000, 10000)

            print(l, end=" ")
        print()

def test03():
    t = 10

    print(t)
    for _ in range(t):
        n = rnd.randint(8001, 10000)
        print(n)

        for _ in range(n):
            l = rnd.randint(-100000, 100000)

            print(l, end=" ")
        print()

def test04():
    t = 5

    print(t)
    for _ in range(t):
        n = rnd.randint(10001, 20000)
        print(n)

        for _ in range(n):
            l = rnd.randint(-1000, 1000)

            print(l, end=" ")
        print()

test04()