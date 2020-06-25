# encoding: utf-8
'''
@author: Aaron_ye
@contact:343342504@qq.com
@file:start_data_analysis.py
@time:2020/5/30 13:14
@desc:
'''

import numpy as np
import pandas as pd
import matplotlib as mpl

import matplotlib.pyplot as plt

data1 = [1, 2, 3, 4, 5]
array1 = np.array(data1)

print data1
print array1

data2 = [[1,2,3],[4,5,6]]
array2 = np.array(data2)

# print data2
# print array2
# print array2.dtype
# array3 = array2.astype('str')
# print array2.dtype
# print array3
# print array3.dtype
t = array2[1]
print t[1]
print array2[0][2]