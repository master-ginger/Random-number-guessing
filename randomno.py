# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 22:51:23 2023

@author: bhava
"""
import random
import math

lower=int(input("Enter the lower bound: "))
upper=int(input("Enter the upper bound: "))


x=random.randint(lower,upper)

guess=round(math.log(upper-lower+1,2))

print("You have only ",guess ," number of guesses")

count=0       
while count<guess:
    count+=1
    n=int(input("Enter any number: "))
    
    if n==x:
        print("Congratulations! You guessed the number")
        break
    elif n<x:
        print("Try again! you are guessing low")
    else:
        print("Try again! you are guessing high")
        
if count>=guess:
    print("Sorry you are out of luck")
    print("The number was ",x)