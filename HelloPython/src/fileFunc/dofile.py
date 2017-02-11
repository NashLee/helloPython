'''
Created on 2016年7月22日

@author: Administrator
'''
from pip._vendor.distlib.compat import raw_input
from _io import open

'读取文件'
fname = raw_input('请输入文件名：')
file = open(fname,'r')
lines = file.readlines()

file.close()    