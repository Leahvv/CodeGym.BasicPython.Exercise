# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 12:30:43 2021

@author: anhtrannh
"""

print("Luu tru file")
num = int(input("Nhap so: "))
clu = 0
if num % 4096 == 0:
    clu = num // 4096
else:
    clu = ( (num // 4096)+ 1)*4
    
print(clu,"KB")
#%%

print("Ma hoa buc thu")


chuoi = input("Chuoi: ")
k = int(input("Nhap:"))
    
if k >= len(chuoi):
    Sb=chuoi
    Se=""
else:
    Sb=chuoi[:k]
    Se=chuoi[k:]

for i in range(len(Sb)-1,-1,-1):
    print(Sb[i],end="")
for y in range(len(Se)-1,-1,-1):
    print(Se[y],end="")
    
#%%
print("Xac dinh chuoi doi xung")
string = str(input("Nhap chuoi:"))
if string == string[::-1]:
    print("Chuoi", string,"la chuoi doi xung")
else:
    print("Chuoi",string,"khong la chuoi doi xung")
#%%
print("Xac dinh chuoi lap")

def check(nho,lon):
    ratio = len(lon)//len(nho)
    if len(lon) % len(nho) == 0:
        if nho * ratio == lon:
            return True
        
string = input ("My string: ")
for i in range (1,len(string)//2+1):
    if check (string[:i],string):
        print(string,"is loop")
        break
else:
    print(string,"is not loop")
#%%
