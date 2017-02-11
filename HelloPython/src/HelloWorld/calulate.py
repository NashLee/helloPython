'''
Created on 2016年7月15日

@author: Administrator
'''
from functools import reduce
def printHello():
    print('Hello World')
def fn(x,y):
    return x*10+y
def fm(x):
    return x*10
fmz = lambda x : x*100

if __name__ == '__main__':
    arr = []
    arr.append(1)
    arr.append(2300)
    arr.append(3)
    arr.append(4)
    arr.append(5)
    mapresult = map(fm,arr)
    
    print(list(mapresult))
    
    
