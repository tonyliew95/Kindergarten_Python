# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 21:33:17 2021

@author: tonyl
"""

myUniqueList = []


def AddList(param1):
    
    if param1 in myUniqueList:
        AddLeftovers(param1)
        return False
    else:
        myUniqueList.append(param1)
        return True
    
def AddLeftovers(param1):
    myLeftovers = []
    myLeftovers.append(param1)
    
AddList(1)
print(myUniqueList)  
AddList(2)
print(myUniqueList)  
AddList(1)
print(myUniqueList)    
AddList(3)
print(myUniqueList)    
AddList(4)
print(myUniqueList)    
AddList(3)
print(myUniqueList) 