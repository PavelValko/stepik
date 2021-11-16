# Task 1
X = int(input())
h = X // 60
m = X % 60
print(h)
print(m)


# Task 2
X = int(input())
H = int(input()) * 60
M = int(input())
result = X + H + M
print(result // 60)
print(result % 60)


# Task 3
A = int(input())
B = int(input())
H = int(input())

if H >= A and H <= B:
    print("Это нормально")
elif H > B:
    print("Пересып")
else:
    print("Недосып")


# Task 4
x = int(input())
n = x % 4 == 0 and x % 100 != 0
if n or x % 400 == 0:
    print("Високосный")
else:
    print("Обычный")


# Task 5
a = int(input())
b = int(input())
c = int(input())
p = (a + b + c) / 2
s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
print(s)


# Task 6
x = int(input())
n = -15 < x <= 12 or 14 < x < 17 or x >= 19
print(n)


# Task 7
a = float(input())
b = float(input())
operation = input()
if operation == "+":
    print(a + b)
elif operation == "-":
    print(a - b)
elif operation == "/" or operation == "mod" or operation == "div":
    if a == 0 or b == 0:
        print("Деление на 0!")
    else:
        if operation == "mod":
            print(a % b)
        elif operation == "div":
            print(a // b)
        else:
            print(a / b)
elif operation == "*":
    print(a * b)
elif operation == "pow":
    print(pow(a, b))


# Task 8
figure = input()
if figure == "треугольник":
    a = float(input())
    b = float(input())
    c = float(input())
    p = (a + b + c) / 2
    S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print(S)
elif figure == "прямоугольник":
    a = float(input())
    b = float(input())
    print(a * b)
elif figure == "круг":
    r = float(input())
    print(3.14 * pow(r, 2))


# Task 9
a = int(input())
b = int(input())
c = int(input())
print(max(a, b, c))
print(min(a, b, c))
print((a + b + c) - (max(a, b , c) + min(a, b, c)))


# Task 10
n = input()
a = int(n) % 10 == 2 and int(n) % 100 != 12
b = int(n) % 10 == 3 and int(n) % 100 != 13
c = int(n) % 10 == 4 and int(n) % 100 != 14
ist = int(n) % 10 == 1 and int(n) % 100 != 11
ista = a or b or c

if ist:
    print(n + ' программист')
elif ista:
    print(n + ' программиста')
else:
    print(n + ' программистов')


# Task 11
number = str(input())
first_sum = int(number[0]) + int(number[1]) + int(number[2])
second_sum = int(number[3]) + int(number[4]) + int(number[5])

if first_sum == second_sum:
    print('Счастливый')
else:
    print('Обычный')