def intreverse(n):
    revno = 0
    while n != 0:
        r = n % 10
        revno = revno * 10 + r
        n = n // 10
    return revno


def matched(n):
    n = list(n)
    c = 0
    for i in range(len(n)):
        if c == -1:
            return False
        if n[i] == "(":
            c = c + 1
        if n[i] == ")":
            c = c - 1
    if c == 0:
        return True
    else:
        return False


def sumprimes(l):
    s = 0
    for i in l:
        if i < 1:
            s = s + 0
        else:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                s = s + i
    return s


import ast


def tolist(inp):
    inp = "[" + inp + "]"
    inp = ast.literal_eval(inp)
    return (inp[0], inp[1])


def parse(inp):
    inp = ast.literal_eval(inp)
    return (inp)


fncall = input()
lparen = fncall.find("(")
rparen = fncall.rfind(")")
fname = fncall[:lparen]
farg = fncall[lparen + 1:rparen]

if fname == "intreverse":
    arg = parse(farg)
    print(intreverse(arg))
elif fname == "matched":
    arg = parse(farg)
    print(matched(arg))
elif fname == "sumprimes":
    arg = parse(farg)
    print(sumprimes(arg))
else:
    print("Function", fname, "unknown")


def intreverse(n):
    ans = 0
    while n > 0:
        (d, n) = (n % 10, n // 10)
        ans = 10 * ans + d
    return (ans)


def matched(s):
    nested = 0
    for i in range(0, len(s)):
        if s[i] == "(":
            nested = nested + 1
        elif s[i] == ")":
            nested = nested - 1
            if nested < 0:
                return (False)
    return (nested == 0)


def factors(n):
    factorlist = []
    for i in range(1, n + 1):
        if n % i == 0:
            factorlist = factorlist + [i]
    return (factorlist)


def isprime(n):
    return (factors(n) == [1, n])


def sumprimes(l):
    sum = 0
    for i in range(0, len(l)):
        if isprime(l[i]):
            sum = sum + l[i]
    return (sum)


import ast


def tolist(inp):
    inp = "[" + inp + "]"
    inp = ast.literal_eval(inp)
    return (inp[0], inp[1])


def parse(inp):
    inp = ast.literal_eval(inp)
    return (inp)


fncall = input()
lparen = fncall.find("(")
rparen = fncall.rfind(")")
fname = fncall[:lparen]
farg = fncall[lparen + 1:rparen]

if fname == "intreverse":
    arg = parse(farg)
    print(intreverse(arg))
elif fname == "matched":
    arg = parse(farg)
    print(matched(arg))
elif fname == "sumprimes":
    arg = parse(farg)
    print(sumprimes(arg))
else:
    print("Function", fname, "unknown")


def contracting(l):
    differences = [abs(l[i] - l[i + 1]) for i in range(len(l) - 1)]
    for i in range(len(differences) - 1):
        if differences[i] <= differences[i + 1]:
            return False
    return True


def counthv(l):
    hc = 0
    vc = 0
    for i in range(1, len(l) - 1):
        if l[i] > l[i - 1] and l[i] > l[i + 1]:
            hc += 1
        elif l[i] < l[i - 1] and l[i] < l[i + 1]:
            vc += 1
    return [hc, vc]


def leftrotate(m):
    n = len(m)
    rotated = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotated[n - 1 - j][i] = m[i][j]
    return rotated


import ast


def parse(inp):
    inp = ast.literal_eval(inp)
    return (inp)


fncall = input()
lparen = fncall.find("(")
rparen = fncall.rfind(")")
fname = fncall[:lparen]
farg = fncall[lparen + 1:rparen]

if fname == "contracting":
    arg = parse(farg)
    print(contracting(arg))

if fname == "counthv":
    arg = parse(farg)
    print(counthv(arg))

if fname == "leftrotate":
    arg = parse(farg)
    savearg = arg
    ans = leftrotate(arg)
    if savearg == arg:
        print(ans)
    else:
        print("Side effect")


# -------------------------------------------------------------------------------------------------------------------
def frequency(l):
    dl1 = set(l)
    dl = list(dl1)
    newl = []
    for i in dl:
        newl.append(l.count(i))
    mi = min(newl)
    ma = max(newl)
    mil = []
    mal = []
    for j in range(len(newl)):
        if newl[j] == mi:
            mil.append(dl[j])
        if newl[j] == ma:
            mal.append(dl[j])
    mil.sort()
    mal.sort()
    return (mil, mal)


def onehop(l):
    new = []
    l.sort()
    for i in range(len(l)):
        for j in range(len(l)):
            if l[i] != l[j]:
                if l[i][1] == l[j][0]:
                    q = l[i][0]
                    w = l[j][1]
                    if q != w:
                        t = [q, w]
                        t = tuple(t)
                        if t not in new:
                            new.append(tuple(t))
    new.sort()
    return (new)


import ast


def parse(inp):
    inp = ast.literal_eval(inp)
    return (inp)


fncall = input()
lparen = fncall.find("(")
rparen = fncall.rfind(")")
fname = fncall[:lparen]
farg = fncall[lparen + 1:rparen]

if fname == "frequency":
    arg = parse(farg)
    print(frequency(arg))

if fname == "onehop":
    arg = parse(farg)
    print(onehop(arg))
