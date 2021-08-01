# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 15:00:56 2021

@author: tonyl
"""
count = 1 

while count <= 100 :

    if count%3 == 0 and count%5 == 0:
        print ("FizzBuzz")
    elif count%5 == 0 :
        print("Bizz")
    elif count%3 == 0  :
        print("Fizz")
    else:
        print(count)
        
    count = count + 1 