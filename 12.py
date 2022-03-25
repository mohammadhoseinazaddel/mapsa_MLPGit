import sys

sys.setrecursionlimit(11500)
ans = 0
# global s
s = 0
# global i
i = 1
X = set()


def f3(i):
    i += 1
    # print("i: ", i)
    f4(i)


def f4(i):
    if i == 10:
        global ans
        ans += s
        f5(i)
    else:
        f3(i)  # go to 3


def f5(i):
    i -= 1
    # print("i: ", i)
    f6(i)


def f6(i):
    if i == 0:
        print("ans: ",ans)
        # print("i: ",i)
    else:
        f7(i)


def f7(i):
    if i not in X:
        f9(i)
    else:
        f8(i)


def f8(i):
    X.remove(i)
    global s
    s -= i
    f5(i)


def f9(i):
    X.add(i)
    global s
    s += i
    f3(i)


f3(i)