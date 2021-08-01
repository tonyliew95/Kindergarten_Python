# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 18:28:38 2021

@author: tonyl
"""

def playboad(rows, column):
    for k in range(rows):
        strings = ""

        for i in range(column - 1):
            strings = strings + "   |"
        print(strings)
        
        if(k < rows - 1):
            strings = "" 
            for j in range(column - 1):
                strings = strings + "-----"
            print(strings)  
    
    return print(True)
             
playboad(6, 6)
