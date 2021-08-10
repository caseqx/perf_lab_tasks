# -*- coding: utf-8 -*-


nums = []

file = open(input(), "r")

lines = file.readlines()

for line in lines:
    nums.append(int(line))
    
file.close

nums2d = []
    
for i in range(len(nums)):
    summa = 0
    row = 0
    for j in range(len(nums)):
        row = abs(nums[i] - nums[j])
        summa = row + summa
    nums2d.append(summa)

print(min(nums2d))