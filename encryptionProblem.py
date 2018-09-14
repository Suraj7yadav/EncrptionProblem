#!/bin/python3

import string
import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    n = len(s)
    print(n)
    new = []
    low = math.floor(math.sqrt(n))
    high = math.ceil(math.sqrt(n))
    flag=0
    z = 0
    if(high*low<n):
        low=low+1
        flag=1
    if(high*low==n and (high==low)):
        z=1
    k=0
    for i in s:
        if(i.isalpha() and i!=' '):
            new.append(i)
    str1 = ''.join(new)
    print(str1)
    print(low)
    print(high)
    #new1 = [[],[]]
    new1 = [['' for x in range(low)] for y in range(high)]
    i = 0
    j = 0
    l=0
    for k in str1: 
        print(k)
        if(l==low+1 or (l==low and (flag==1 or z==1))):
            l=0
            i=0
            j+=1
            #continue
        new1[i][j] = k
        print(new1)
        i+=1
        l+=1
    final = ''
    for i in range(0,high):
        stri = ''.join(new1[i])
        if(i==0):
            final = final + stri
        else:
            final = final + " " + stri
    return(final)
    print(final)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
