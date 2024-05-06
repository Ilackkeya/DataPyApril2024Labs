#!/usr/bin/env python
# coding: utf-8

# In[18]:


# solveMeFirst
def solveMeFirst(a,b):
    # Hint: Type return a+b below
    return a+b


num1 = int(input())
num2 = int(input())
res = solveMeFirst(num1,num2)
print(res)


# In[22]:


# SimpleArraysum
import math
import os
import random
import re
import sys

#
# Complete the 'simpleArraySum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ar as parameter.
#

def simpleArraySum(ar):
    # Write your code here
    add =0
    for i in range(len(ar)):
        add+= ar[i]
    
    return add
        

if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)
    
    print(result)

#     fptr.write(str(result) + '\n')

#     fptr.close()


# In[17]:


#plusMinus

#Method 1

def plusMinus(arr):
    # Write your code here
    count_pos = 0
    count_neg = 0 
    count = 0
    
    for i in range(n):
        if arr[i] > 0:
            count_pos += 1
            ratio_pos = count_pos/n
        elif arr[i]< 0:
            count_neg += 1
            ratio_neg = count_neg/n
        else:
            count+=1
            ratio = count/n
            
    print("{:.6f}".format(ratio_pos)) 
    print("{:.6f}".format(ratio_neg))
    print("{:.6f}".format(ratio))


n = int(input().strip())

arr = list(map(int, input().rstrip().split()))

plusMinus(arr)


# In[24]:


#Method 2

def plusMinus(arr):    
    n = len(arr)
    ratio_pos = (sum(1 for i in arr if i>0)/n)
    ratio_neg = (sum(1 for i in arr if i<0)/n)
    ratio = (sum(1 for i in arr if i==0)/n)
    print("{:.6f}".format(ratio_pos)) 
    print("{:.6f}".format(ratio_neg))
    print("{:.6f}".format(ratio))


n = int(input().strip())

arr = list(map(int, input().rstrip().split()))

plusMinus(arr)


# In[23]:


# staircase

def staircase(n):
    # Write your code here
    for i in range(1, n+1):
#         space = ' '*(n-1) 
#         step = i*'#'
#         stair_step = space+step
#         print(stair_step)
        step =' '*(n-1) + i*'#'
        print(step)
        n-=1


n = int(input().strip())
staircase(n)

