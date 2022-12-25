import random

n = int(input())
a = []

for i in range(n):
    a.append(random.randint(0,1))

zero = a.count(0)/len(a)
ones = a.count(1)/len(a)

c = 0
t = 0

for x in range(len(a)-1):
    if a[c] != a[c+1]:
        t += 1
    c += 1

print(a)
print(zero, ones)
print(1 - t/len(a))
