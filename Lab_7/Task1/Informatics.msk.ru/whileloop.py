#1

n = int(input())
i = 1
while i * i <= n:
    print(i * i)
    i += 1

#2

n = int(input())
i = 2
while n % i != 0:
    i += 1
print(i)

#3

n = int(input())
p = 1
while p <= n:
    print(p)
    p *= 2

#4

n = int(input())
k = 0
p = 1
while p < n:
    p *= 2
    k += 1
print(k)