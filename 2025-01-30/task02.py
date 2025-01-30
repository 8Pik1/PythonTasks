x = int(input("Введите число: "))
n = int(input("Введите количество повторов: "))
sum0 = 0

for _ in range(n):
    sum0 += x
print(sum0)

sum1 = 0
s = n
while n > 0:
    sum1 += x
    s -= 1
print(sum1)
