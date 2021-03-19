# -*- coding: utf-8 -*-

def solution(nums):
    l = len(nums)
    if l == 0: return []
    if l == 1: return [1]

    for i in range(l):
        if i == 0:
            if nums[i] < nums[i+1]: nums[i] = 1
            else: nums[i] = nums[i+1] + 1
        elif i == l - 1:
            if nums[i] < nums[i-1]: nums[i] = 1
            else: nums[i] = nums[i-1] + 1
        else:
            if nums[i] < nums[i-1] and nums[i] < nums[i+1]: nums[i] = 1
            elif nums[i] > nums[i-1] and nums[i] > nums[i+1]: nums[i] = max(nums[i-1], nums[i+1]) + 1
            else: nums[i] = min(nums[i-1], nums[i+1]) + 1
    for i in range(l-1, -1, -1):
        if i == 0:
            if nums[i] < nums[i+1]: nums[i] = 1
            else: nums[i] = nums[i+1] + 1
        elif i == l - 1:
            if nums[i] < nums[i-1]: nums[i] = 1
            else: nums[i] = nums[i-1] + 1
        else:
            if nums[i] < nums[i-1] and nums[i] < nums[i+1]: nums[i] = 1
            elif nums[i] > nums[i-1] and nums[i] > nums[i+1]: nums[i] = max(nums[i-1], nums[i+1]) + 1
            else: nums[i] = min(nums[i-1], nums[i+1]) + 1
        
    return nums


if __name__ == '__main__':
    nums = [3,2,5,7,4,8,3,5,7,1,3] # 2 1 2 3 1 2 1 2 3 1 2
    res = solution(nums)
    for x in res:
        print(x, end=' ')