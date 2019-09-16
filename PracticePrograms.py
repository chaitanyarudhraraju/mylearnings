import os, sys
import time
import re


#1.Subarray with given sum

def subarraysum(array, s):
    for i in xrange(len(array)):
        j = i + 1
        count = array[i]
        while j < len(array):
            count += array[j]
            if count == s:
                print i + 1, j + 1
                return i, j
            elif count < s:
                j += 1
                continue
            else:
                break
    print -1
subarraysum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 15)

#2. Count the triplets
#Given an array of distinct integers.
#The task is to count all the triplets such that sum of two elements equals the third element.


def counttriplet(array):
    array.sort()
    print array
    n = len(array)
    i = n-1
    count = 0
    while i >= 0:
        j = 0
        k = i-1
        #print k
        while j < k:
            print array[i]
            if array[i] == array[j] + array[k]:
                print array[i], array[j], array[k]
                count += 1
                break
            elif array[j] + array[k] < array[i]:
                j += 1
            else:
                k -= 1
        i -= 1

counttriplet([1, 7, 5, 12, 8, 13, 15])

#Given an array arr of N integers. Find the contiguous sub-array with maximum sum.

def maxsubarraycount(array):
    count = 0
    i = 0
    n = len(array)
    subcount = array[i]
    while i < n:
        j = i
        count = 0
        while j < n:
            count += array[j]
            if count > subcount:
                subcount = count
            j += 1
        i += 1
    print subcount

maxsubarraycount([-2, -3, 4, -1, -2, 1, 5, -3])

def merge_sorted_arrays(arr1, arr2):

     m, n = len(arr1), len(arr2)
     i, j = 0, 0
     arr = []
     while i < m and j < n:
         if arr1[i] >= arr2[j]:
             arr.append(arr2[j])
             j += 1
         else:
             arr.append(arr1[i])
             i += 1
     while i < m:
           arr.append(arr1[i])
           i += 1
     while j < n:
           arr.append(arr2[j])
           j += 1

     print(arr)

merge_sorted_arrays([1,3,5,7,7], [2,4,5,6,8,10])

def rearrange_array(a):
    pass

def num_of_pairs(a, b):
    pass
def inversion_count_array(a):
        i, j = 0, 1
        count = 0
        print a
        while i < len(a):
            if j == len(a):
                i += 1
                j = i + 1
            elif a[i] > a[j]:
                 count += 1
                 j += 1
            else: j += 1
        print "count:", count
        return count

inversion_count_array([2, 4, 6, 1, 3, 5])

#Sort an array of 0s, 1s and 2s

def sort_zero_one(a, n):
    k = 0
    while k <= n:
        j = k+1
        if j == n:
            break
        while j >= 0:
            i = j-1
            if not a[i] <= a[j]:
                a[i], a[j] = a[j], a[i]
                j -= 1
                i -= 1
                if a[i] <= a[j] or i == 0:                                                  
                    break
            else:
                j -= 1
        k += 1
    print a

sort_zero_one([0, 2, 1, 2, 0, 0, 0], 7)

def equ_point(a):
    if len(a) == 1:
        return 1
    else:
        i = 1
        while i < len(a)-1:
            j = i-1
            k = i+1
            count = a[j]
            count1 = a[k]
            while j >= 0 or k <= len(a)-1:
                j -= 1
                if not j < 0:
                    count += a[j]
                k += 1
                if not k > len(a)-1:
                   count1 += a[k]
            if count == count1:
                print 1
            i += 1
print equ_point([-7, 1, 5, 2, -4, 3, 0])


def array_leaders(a, n):
    pass

def train_problem(a, d):
    Atime = [int('%02d'%j + '%02d'%i)  for j in range(24) for i in range(60)]
    Dtime = [int('%02d'%j + '%02d'%i)  for j in range(24) for i in range(60)]
    i = 1
    j = 0
    platCount = 1
    while i < len(a) and j < len(d):        
        if not a[i] < d[j]:
            platCount += 1
        i += 1
        j += 1
    print "******",platCount
    
arr = [900, 940, 950, 1100, 1500, 1800, 1700]
dep = [910, 1200, 1120, 1130, 1900, 2000, 2100]            
train_problem(arr, dep)

def sub_array_reverse(a, k):
    n = len(a)
    i = 0    
    while i < n:
        left = i 
        right = min(i+k-1, n-1)
        while(left < right):
            a[left], a[right] = a[right], a[left] 
            left += 1
            right -= 1
        i += k
    print a
        
sub_array_reverse([10, 20, 30, 40, 50, 60], 3)

def k_smallest_position(arr, k):
    eleCount = len(arr) - k
    n = len(arr)
    i = 0
    while i < n:
        j = 0
        count = 0
        while j < n:                    
            if not arr[i] == arr[j] and arr[j] > arr[i]:                       
                count += 1
            j += 1
        if count == eleCount:
            break               
        i += 1
    print arr[i]
    return arr[i] 
               
k_smallest_position([7, 10, 4, 20, 15], 4)    


def rain_water_trapped(a,n):
    start_point = 0
    end_point = 1       
    i = 0
    j = 1
    count = 0  
    while j < n:
        
        if a[i] > a[j]:
            print "check...-> 1"
            if j >= i+1:
               print i,j
               count += a[i]-a[j]
            start_point = i
            j += 1
                                       
        elif a[i] <= a[j] or j == i+1:
            print "check...-> 2"                    
            i += 1           
            j += 1
        else:
            break
    print count
        
   
            
rain_water_trapped([3,0,2,4], 4)



''

