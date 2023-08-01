#Первое задание
from random import randint
a=int(input("10.Введите число подбрасываний: "))
m=[]
for i in range(0,a):
    m.append(randint(0, 1))
print(m)
sum=0
for y in range(0,len(m)):
    if m[y]==0:
        sum=sum+1
print(sum)
#Второе задание
s = int(input("12.Задай сумму двух чисел: "))
p = int(input("Задай произведение чисел: "))
for x in range(s):
    for y in range(p):
        if s == x + y and p == x * y:
            print(f'первое число = {x}, второе число = {y}')

#Третье задание

x=int(input("14.Введите число: "))
o=1
m3=[]
while o < x:
    m3.append(o)
    o=o*2
print(m3)