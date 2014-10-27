# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
C:\Users\Yuanze LEO\.spyder2\.temp.py
"""
from math import *
c = [1]*2000025
a = [2]
#Q1:sum 1000
def sum1000(n):
    count = 0
    #initialize count
    for i in range(n-1):
        if (i+1)%3 ==0 or (i+1)%5 == 0:
            count += (i+1)
    return count
#Q2:sum the prime numbers in 2000000
#use shai method to pick up prime numbers
def shaifa(n):
    sums = 2
    for i in range(3,n,2):
        if c[i] == 1:
            count = i*2
            while count<n:
               c[count] = 0
               count += i
            a.append(i)
            sums += i
    print sums
#Q3：



#judge if the year is leapyear,and return the day of months
def monthdays_of_year(year):
    monthdays = [31,28,31,30,31,30,31,31,30,31,30,31]
    if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
        monthdays[1] = 29
        return monthdays
    else:
        return monthdays

def Q3():       
    c_Sunday = 0
    p_days = 1
    for n in range(12):
        p_days += monthdays_of_year(1900)[n]
    for year in range(1901,2001):
        for month in range(12):
    
            if p_days % 7 == 0:
                c_Sunday += 1
            p_days += monthdays_of_year(year)[month]
    print c_Sunday

print sum1000(1000)
shaifa(2000000)
Q3()
#Q4:
#use the 'a' list from Q2 to finish Q4
def Q4():
    count = 1
    #create a list called bools to marked the prime that have been checked
    for i in range(0,len(a)):
        e = a[i]
        if (e>=1000)and (c[e]== 0):
            break
        else:
          m = str(e)
          k = len(m)-1
          d = k
          if ('0' in m) or ('2' in m) or ('4' in m) or ('6' in m) or ('8' in m):
              continue
          m = m + m
          #check if i is a looping prime
          while k>0:
              w = int(m[(1+d-k):(1+d-k+d+1)])
              if w >=1000000:
                  break
              #print c,'   ',k,'***',i
              if c[w]==0:
                  break
              k -= 1
          else:
              count += 1
    print count           

Q4()
