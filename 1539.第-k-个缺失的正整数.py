#
# @lc app=leetcode.cn id=1539 lang=python3
#
# [1539] 第 k 个缺失的正整数
#
# https://leetcode-cn.com/problems/kth-missing-positive-number/description/
#
# algorithms
# Easy (53.69%)
# Likes:    38
# Dislikes: 0
# Total Accepted:    11.4K
# Total Submissions: 21.2K
# Testcase Example:  '[2,3,4,7,11]\n5'
#
# 给你一个 严格升序排列 的正整数数组 arr 和一个整数 k 。
# 
# 请你找到这个数组里第 k 个缺失的正整数。
# 
# 
# 
# 示例 1：
# 
# 输入：arr = [2,3,4,7,11], k = 5
# 输出：9
# 解释：缺失的正整数包括 [1,5,6,8,9,10,12,13,...] 。第 5 个缺失的正整数为 9 。
# 
# 
# 示例 2：
# 
# 输入：arr = [1,2,3,4], k = 2
# 输出：6
# 解释：缺失的正整数包括 [5,6,7,...] 。第 2 个缺失的正整数为 6 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= arr.length <= 1000
# 1 <= arr[i] <= 1000
# 1 <= k <= 1000
# 对于所有 1 <= i < j <= arr.length 的 i 和 j 满足 arr[i] < arr[j] 
# 
# 
#

# @lc code=start
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        if arr[0] - 1 >= k:
            return k
        
        if arr[-1] - len(arr) < k:
            return k + len(arr)
        '''
        # 顺序查找：
        for i in range(len(arr)-1):
            if arr[i] - i - 1  < k and arr[i+1] - i - 2 >= k:
                return k + i + 1
        '''
        # 二分查找
        l, r = 0, len(arr)-1
        while l < r:
            mid = l + (r - l) // 2
            if arr[mid] - mid - 1 < k and arr[mid+1] - mid - 2 >= k:
                return k + mid + 1
            if arr[mid] - mid - 1 >= k:
                r = mid
            else:
                l = mid + 1
        return k + l + 1

# @lc code=end

