# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 20:46:57 2020

@author: 14052
"""

def binary_search(numbers_list, number):
    left_ind = 0
    right_ind = len(numbers_list)-1
    mid_ind = 0
    
    while left_ind <= right_ind:
    
        mid_ind = (left_ind + right_ind) // 2
    
        mid_number = numbers_list[mid_ind]
        
        if mid_number == number:
            return mid_ind
        if mid_number < number:
            left_ind = mid_ind + 1
        else:
            right_ind = mid_ind - 1
            
    return -1

def linear_search(numbers_list, number):
    for ind,ele in enumerate(numbers_list):
        if ele == number:
            return ind
    return "Not in List"


if __name__ == "__main__":
    numbers_list = [12,15,17,19,21,24,45,67]
    number = 12
    
    index = binary_search(numbers_list, number)
    
    print(f"Number found at {index} using binary search")