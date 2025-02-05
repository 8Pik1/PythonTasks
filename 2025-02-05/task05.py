def fun(a):
    s = a + fun(a - 1)
    return s

i = int(input())
r = fun(i)
print(r)
