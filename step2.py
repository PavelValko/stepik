# Task 1
n = int(input())
s = 0
while n != 0:
    s = s + n
    n = int(input())
print(s)


# Task 2
a = int(input())
b = int(input())
d = 0
while d <= (a * b):
    d += 1
    if d % a == 0 and d % b == 0:
        print(d)
        break


# Task 3
while True:
    n = int(input())
    if n > 100:
        break
    elif n < 10:
        continue
    else:
        print(n)


# Task 4
a = int(input())
b = int(input())
c = int(input())
d = int(input())
for i in range(c, d + 1):
    print(' ', end='\t')
    print(i, end='')
print()
for i in range(a, b + 1):
    print(i, end='\t')
    for j in range(c, d + 1):
        print(i * j, end='\t')
    print()


# Task 5
a = int(input())
b = int(input())
s = 0
count = 0
for i in range(a, b + 1):
    if i % 3 == 0:
        count +=1
        s += i
s = s / count
print(s)


# Task 6
string = str(input())
count = 0
length = len(string)
for i in string.lower():
    if i == 'g' or i == 'c':
        count += 1
gc = (count / length) * 100
print(gc)


# Task 7
s = str(input())
new_s = ''
count = 1
new_s += s[0]
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        count += 1
    else:
        if count >= 1:
            new_s += str(count)
        new_s += s[i+1]
        count = 1
if count >= 1:
    new_s += str(count)
print(new_s)


# Task 8
s = str(input())
result = 0
for i in s.split():
    result = result + int(i)
print(result)


# Task 9
string = input()
s = string.split()
n = s[-1]
for i in range(len(s)-1):
    if i == 0:
        print(str(int(s[-1]) + int(s[1])), end=' ')
    else:
        print(str(int(s[i-1]) + int(s[i+1])), end=' ')
if len(s) == 1:
    print(s[0])
elif n == s[-1] and len(s) > 1:
    print(str(int(s[-2]) + int(s[0])), end='')


# Task 10
s = [i for i in input().split()]
for i in set(s):
    if s.count(i) > 1:
        print(i, end=' ')


# Task 11
sum = 0
sum_of_square = 0
while True:
    number = int(input())
    sum += number
    sum_of_square += (number**2)
    if sum == 0:
        print(sum_of_square)
        break


# Task 12
n = int(input())
new_s = []
result = []
if n == 1:
    print(n)
else:
    for i in range(1, n+1):
        new_s += ([i] * i)
        if len(new_s) > n:
            print(*new_s[:n])
            break


# Task 13
lst = [int(i) for i in input().split()]
x = int(input())
for i in range(len(lst)):
    if x == lst[i]:
        print(i, end=' ')
if x not in lst:
    print('Отсутствует')


# Task 14
a = []
b = input()
while b != 'end':
    a.append([int(i) for i in b.split()])
    b = input()
l = len(a)
for i in range(l):
    li = len(a[i])
    for j in range(li):
        new_arr = (a[i-l+1][j] + a[i-1][j] + a[i][j-li+1] + a[i][j-1])
        print(new_arr, end=' ')
    print()


# Task 15
n = int(input())
lst = [[0 for i in range(n)] for j in range(n)]
a = 1
low = 0
high = n - 1
count = int((n + 1) / 2)

for i in range(count):
    for j in range(low, high+1):
        lst[i][j] = a
        a = a + 1
    for j in range(low+1, high+1):
        lst[j][high] = a
        a = a + 1
    for j in range(high-1, low-1, -1):
        lst[high][j] = a
        a = a + 1
    for j in range(high-1, low, -1):
        lst[j][low] = a
        a = a + 1
    low = low + 1
    high = high - 1

for i in range(n):
    for j in range(n):
        print(lst[i][j], end=' ')
    print()    