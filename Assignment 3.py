# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def ifStatement(param1,param2,param3):
    
    param1 = int(param1)
    param2 = int(param2)
    param3 = int(param3)
    
    if param1 == param2 or param1 == param3  or param2 == param3:
        return True
    else:
        return False
    

print(ifStatement(6,"5",5))
    