#1

print("Hello, World!")

#2

n = int(input())

if n % 2 == 1:
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")

#3

a = int(input())
b = int(input())

print(a + b)
print(a - b)
print(a * b)

#4

print(a // b)
print(a / b)

#5

for i in range(n):
    print(i*i)

#6

for i in range(1, n+1):
    print(i, end="")

#7

x = int(input())
y = int(input())
z = int(input())

result = [[i, j, k] 
          for i in range(x+1) 
          for j in range(y+1) 
          for k in range(z+1) 
          if i + j + k != n]

print(result)

#8

arr = int(input())

arr = list(arr)

max_score = max(arr)

arr = [x for x in arr if x != max_score]

print(max(arr))

#9

students = []

for _ in range(int(input())):
    name = input()
    score = float(input())
    students.append([name, score])

scores = sorted(set([s[1] for s in students]))
second_lowest = scores[1]

names = [s[0] for s in students if s[1] == second_lowest]

for name in sorted(names):
    print(name)

#10

print(a + b)
print(a - b)
print(a * b)