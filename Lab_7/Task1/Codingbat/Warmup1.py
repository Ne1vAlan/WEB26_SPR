#1

def sleep_in(weekday, vacation):
    return not weekday or vacation

#2

def diff21(n):
    if n > 21:
        return (n - 21) * 2
    return abs(n - 21)

#3

def near_hundred(n):
    return abs(100 - n) <= 10 or abs(200 - n) <= 10

#4

def missing_char(str, n):
    return str[:n] + str[n+1:]

#5

def monkey_trouble(a_smile, b_smile):
    return a_smile == b_smile

#6

def parrot_trouble(talking, hour):
    return talking and (hour < 7 or hour > 20)

#7

def pos_neg(a, b, negative):
    if negative:
        return a < 0 and b < 0
    return (a < 0 and b > 0) or (a > 0 and b < 0)

#8

def front_back(str):
    if len(str) <= 1:
        return str
    return str[-1] + str[1:-1] + str[0]

#9

def sum_double(a, b):
    if a == b:
        return 2 * (a + b)
    return a + b

#10

def makes10(a, b):
    return a == 10 or b == 10 or a + b == 10

#11

def not_string(str):
    if str.startswith("not"):
        return str
    return "not " + str

#12

def front3(str):
    front = str[:3]
    return front * 3
