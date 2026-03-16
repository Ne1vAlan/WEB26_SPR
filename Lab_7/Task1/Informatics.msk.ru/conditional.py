#1

a = int(input())
b = int(input())
print(max(a, b))

#2

n = int(input())
if (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0):
    print("YES")
else:
    print("NO")

#3

a = int(input())
b = int(input())
if (a == 1) == (b == 1):
    print("YES")
else:
    print("NO")

#4

x = int(input())
if x > 0:
    print(1)
elif x < 0:
    print(-1)
else:
    print(0)

#5

a = int(input())
b = int(input())
if a > b:
    print(1)
elif b > a:
    print(2)
else:
    print(0)