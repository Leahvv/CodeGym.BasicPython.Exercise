# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 20:32:35 2021

@author: anhtrannh
"""
#Exercise1
a = input("Nhap a: ")
b = input("Nhap b: ")

if a.isdigit():
    if b.isdigit():
        a=int(a)
        b=int(b)
        sum = 0
        for i in range(a,b):
            sum = sum + i
            print(sum, end=" ")
        print()
        print("Tong cac so tu",a,"den",b, sum)
    else:
        print("b phai la so")
else:
    print("a phai la so")

#%%
#Exercise2
a = input("Nhap a: ")
b = input("Nhap b: ")

if a.isdigit():
    if b.isdigit():
        a=int(a)
        b=int(b)
        for i in range(a,b):
            if i%15==0:
                print("FizzBuzz",end=" ")
            elif i%3==0:
                print("Fizz",end=" ")
            elif i%5==0:
                print("Buzz",end=" ")
            else:
                print(i,end=" ")
    else:
        print("b phai la so nguyen")
else:
    print("a phai la so nguyen")
#%%
#Excercise3
import random
x = random.randint(1,10)
num = int(input("Enter your number (1-10): "))
count = 0
while count<2:   
    if num == x:
        print("Congratulation!")
        break
    elif num > x:
        print("So nhap lon hon")
        num = int(input("Enter your number: "))
        count = count +1
    else:
        print("So nhap nho hon")
        num = int(input("Enter your number: "))
        count = count +1
else:
    print("Ban het so luot doan. So ngau nhien la:",x)

#%%
#Excercise4
a = input("Nhap a: ")
if a.isdigit():
    a=int(a)
    while a!=0:
        print(a%10,end="")
        a=a//10
else:
    print("a phai la so nguyen")
#%%
#Excercise
num = int(input("Nhap vao so nguyen (>=2): "))
if num == 2:
    print(num,"la so nguyen to")
else:
    for i in range(2,num):
        if num % i == 0:
            print(num,"la so hop to")
            break
        else:
            print(num," la so nguyen to")
            break

#%%
i=1
count = 0;
x = int(input("Enter the number:"))
while (count < x):
    c = 0
    for j in range (1, (i+1), 1):
        a = i%j
        if (a==0):
            c = c+1
    
    if (c==2):
          print (i,end=" ")
          count = count+1
    i=i+1
    
#%%
for i in range (1,6):
    print("*"*i)
#%%
for i in range (5,0,-1):
    print("*"*i)
#%%
for i in range(5,0,-1):
    print(i*" " + "*"*(6-i) )
#%%
for i in range(0,6):
    print(" "*i + (6-i)*"*")
#%%
for row in range(1,11):
    for col in range(1,11):
        print(col*row,end=" ")
    print()