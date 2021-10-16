"""
Given the array of integers nums, 
you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).
"""


a = list(map(int, input().split(',')))
a.sort()
print((a[-1] - 1) * (a[-2] - 1))
