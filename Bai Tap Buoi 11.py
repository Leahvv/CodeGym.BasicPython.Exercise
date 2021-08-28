# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 15:24:21 2021

@author: anhtrannh
"""

import turtle as t
import random

def draw_circle():
    r = int(input("Input r: "))
    sl_circle = int(input("Input sl: "))
    color_circle = input("Input color: ")
    for c in range(sl_circle):
        t.penup()
        t.goto(random.randint(-200, 200),random.randint(-200, 200))
        t.pendown()
        t.fillcolor(str(color_circle))
        t.begin_fill()
        t.circle(r)
        t.end_fill()
    t.done()
    
def draw_rectangular():
    cd = int(input("Input cd: "))
    cr = int(input("Input cr: "))
    sl_rectangular = int(input("Input sl: "))
    color_rectangular = input("Input color: ")
    for rec in range(sl_rectangular):
        t.penup()
        t.goto(random.randint(-200, 200),random.randint(-200, 200))
        t.pendown()
        t.fillcolor(str(color_rectangular))
        t.begin_fill()
        t.forward(cd)
        t.left(90)
        t.forward(cr)
        t.left(90)
        t.forward(cd)
        t.left(90)
        t.forward(cr)        
        t.end_fill()                
    t.done()
    
def draw_square():
    size = int(input("Input size: "))
    sl_square = int(input("Input sl: "))
    color_square = input("Input color: ")
    for squ in range(sl_square):
        t.penup()
        t.goto(random.randint(-200, 200),random.randint(-200, 200))
        t.pendown()
        t.fillcolor(str(color_square))
        t.begin_fill()
        for i in range(4):
            t.forward(size)
            t.right(90)
        t.end_fill()                
    t.done()
    
def draw_pentagon():
    num_edge = int(input("Input edge: "))
    size_pen = int(input("Input size: "))
    sl_pen = int(input("Input sl: "))
    color_pen = input("Input color: ")
    for pen in range(sl_pen):
        t.penup()
        t.goto(random.randint(-200, 200),random.randint(-200, 200))
        t.pendown()
        t.fillcolor(str(color_pen))
        t.begin_fill()
        for i in range(num_edge):
            t.forward(size_pen)
            t.right(360/num_edge)
        t.end_fill()                
    t.done()   

def draw_oval():
    size_oval = int(input("Input size: "))
    sl_oval = int(input("Input sl: "))
    color_oval = input("Input color: ")
    for o in range(sl_oval):
        t.penup()
        t.goto(random.randint(-200, 200),random.randint(-200, 200))
        t.pendown()
        t.fillcolor(str(color_oval))
        t.begin_fill()
        for i in range(2):
            t.circle(size_oval,90)
            t.circle(size_oval/2,90)
        t.end_fill()
    t.done()
    
def menu_choice():
    print("Choose one of the following options?")
    print("   c) Circle")
    print("   r) Rectangular")
    print("   s) Square")
    print("   p) Pentagon")
    print("   o) Oval")
    choice = input("Choice: ")
    if choice.lower() in ['c','r', 's','p', 'o']:
        return choice
    else:
        print(choice +"?")
        print("Invalid option")
        return None

def main_loop():
    
    choice = menu_choice()
    if choice == 'c':
        draw_circle()
    elif choice == 'r':
        draw_rectangular()
    elif choice == 's':
        draw_square()
    elif choice == 'p':
        draw_pentagon()
    elif choice == 'o':
        draw_oval()
    else:
        print("Invalid choice.")

