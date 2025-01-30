n = int(input())
a1 = []
a2 = []
for i in range(n):
    if i % 2 == 0:
        a1.append(i)
    if i % 5 == 0:
        a2.append(i)
print(a1,a2)

a3 = []
i1 = 0
i2 = 0
while i1 < len(a1) or i2 < len(a2):
    if i1 == len(a1):
        a3.append(a2[i2])
        i2 += 1
    elif i2 == len(a2):
        a3.append(a1[i1])
        i1 += 1
    elif a1[i1] == a2[i2]:
        a3.append(a1[i1])
        i1 += 1
        i2 += 1
    elif a1[i1] < a2[i2]:
        a3.append(a1[i1])
        i1 += 1
    else:
        a3.append(a2[i2])
        i2 += 1
    print(a3)
