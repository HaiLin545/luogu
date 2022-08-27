
n = int(input().strip())
p = [list(input().strip()) for i in range(n)]
q = [list(input().strip()) for i in range(n)]


def rotate(a):
    t = [[] for i in range(n)]
    for i in range(n):
        for j in range(n):
            t[i].append(a[n-1-j][i])
    return t


def myReverse(a):
    return [i[::-1] for i in a]


def solve():
    tmp = p
    for i in range(1, 4):
        tmp = rotate(tmp)
        if q == tmp:
            return i
    r = myReverse(p)
    if q == r:
        return 4
    tmp = r
    for i in range(1, 4):
        tmp = rotate(tmp)
        if q == tmp:
            return 5
    if p == q:
        return 6
    return 7


print(solve())
