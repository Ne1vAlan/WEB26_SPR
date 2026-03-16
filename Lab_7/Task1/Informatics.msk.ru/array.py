#1

data = list(map(int, input().split()))
n = data[0]
a = data[1:]
print(*a[::2])

#2

data = list(map(int, input().split()))
n = data[0]
a = data[1:]
print(*[x for x in a if x % 2 == 0])

#3

data = list(map(int, input().split()))
n = data[0]
a = data[1:]
print(sum(1 for x in a if x > 0))

#4

data = list(map(int, input().split()))
n = data[0]
a = data[1:]
print(sum(1 for i in range(1, n) if a[i] > a[i-1]))

#5

data = list(map(int, input().split()))
n = data[0]
a = data[1:]
found = any((a[i] > 0 and a[i+1] > 0) or (a[i] < 0 and a[i+1] < 0) for i in range(n-1))
print("YES" if found else "NO")