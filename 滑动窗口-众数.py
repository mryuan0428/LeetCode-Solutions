# -*- coding: utf-8 -*-
'''
    l = input()
    nums = input().split(' ')
    nums.sort()
    print(' '.join(nums))
'''
if __name__ == "__main__":
    n, k = map(int, input().split(' '))
    nums = list(map(int, input().split(' ')))
    counter = {} # num:次数
    
    # 先处理前k个:
    for i in range(k):
        counter[nums[i]] = counter.get(nums[i],0) + 1
    res = sorted(counter.items(), key=lambda x:(x[1], -x[0]))
    print(res[-1][0])

    i = k
    while i < n:
        counter[nums[i]] = counter.get(nums[i],0) + 1
        counter[nums[i-k]] -= 1
        if counter[nums[i-k]] == 0: counter.pop(nums[i-k])
        
        res = sorted(counter.items(), key=lambda x:(x[1], -x[0]))
        print(res[-1][0])
        i += 1
