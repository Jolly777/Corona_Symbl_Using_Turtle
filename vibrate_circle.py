#!/usr/bin/env python
# coding: utf-8
#python_vibrate_circle
import turtle  
# Creating turtle  
t = turtle.Turtle()  
s = turtle.Screen()  
s.bgcolor("black")  
t.pencolor("green")  
t.shape("turtle")
  
a = 0  
b = 0  
t.speed(0)  
t.penup()  
t.goto(0,200)  
t.pendown()  
while(True):  
    t.forward(a)  
    t.right(b)  
    a+=3  
    b+=1  
    if b == 210:  
        break 
t.penup()
t.goto(20,0)
t.pendown()
t.pencolor("red")
t.write("CORONA-VIRUS", align="CENTER", font=("Dades", 35))
t.penup()
turtle.done()
