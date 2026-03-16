#1

a, b = map(int, input().split())
print(*[i for i in range(a, b+1) if i % 2 == 0])

#2

a, b, c, d = map(int, input().split())
print(*[i for i in range(a, b+1) if i % d == c])

#3

import math
a, b = map(int, input().split())
print(*[i for i in range(a, b+1) if int(math.isqrt(i))**2 == i])

#4

x, d = map(int, input().split())
count = 0
while x > 0:
    if x % 10 == d:
        count += 1
    x //= 10
print(count)

#5

x = int(input())
s = 0
while x > 0:
    s += x % 10
    x //= 10
print(s)

#6

x = int(input())
t = 0
while x > 0:
    t = t * 10 + x % 10
    x //= 10
print(t)

#7

x = int(input())
i = 2
while i * i <= x:
    if x % i == 0:
        print(i)
        break
    i += 1
else:
    print(x)

#8

x = int(input())
print(*[i for i in range(1, x+1) if x % i == 0])

#9

import math
x = int(input())
count = 0
i = 1
while i * i <= x:
    if x % i == 0:
        count += 2
        if i * i == x:
            count -= 1
    i += 1
print(count)

#10

s = 0
for _ in range(100):
    s += int(input())
print(s)

#11

data = list(map(int, input().split()))
n = data[0]
print(sum(data[1:n+1]))

#12

n = input().strip()
result = 0
for bit in n:
    result = result * 2 + int(bit)
print(result)

#13

data = list(map(int, input().split()))
n = data[0]
print(data[1:n+1].count(0))