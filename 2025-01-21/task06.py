n = 100
a = 2
while a < n:
    i = 2
    isSimple = True
    while i <= a - 1:
        if a % i == 0:
            isSimple = False
            break
        i += 1
    if isSimple:
        print(a)
    a += 1
