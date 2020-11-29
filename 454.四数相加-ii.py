#
# @lc app=leetcode.cn id=454 lang=python3
#
# [454] 四数相加 II
#
# https://leetcode-cn.com/problems/4sum-ii/description/
#
# algorithms
# Medium (56.77%)
# Likes:    297
# Dislikes: 0
# Total Accepted:    51.4K
# Total Submissions: 89.2K
# Testcase Example:  '[1,2]\n[-2,-1]\n[-1,2]\n[0,2]'
#
# 给定四个包含整数的数组列表 A , B , C , D ,计算有多少个元组 (i, j, k, l) ，使得 A[i] + B[j] + C[k] +
# D[l] = 0。
# 
# 为了使问题简单化，所有的 A, B, C, D 具有相同的长度 N，且 0 ≤ N ≤ 500 。所有整数的范围在 -2^28 到 2^28 - 1
# 之间，最终结果不会超过 2^31 - 1 。
# 
# 例如:
# 
# 
# 输入:
# A = [ 1, 2]
# B = [-2,-1]
# C = [-1, 2]
# D = [ 0, 2]
# 
# 输出:
# 2
# 
# 解释:
# 两个元组如下:
# 1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
# 2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
# 
# 
#

# @lc code=start
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        
        # 想法1: 暴力搜索: O(N^4)
        def exhaustiveSearch():
            res = 0
            for i in range(len(A)):
                for j in range(len(B)):
                    for k in range(len(C)):
                        for l in range(len(D)):
                            if A[i] + B[j] + C[k] + D[l] == 0:
                                res += 1
            return res
        
        ''' 想法2:
            分组 + 哈希表
            可以将四个数组分成两部分，A 和 B 为一组，C 和 D 为另外一组。
            得到所有 A[i]+B[j] 的值并存入哈希映射中。键表示一种 A[i]+B[j]
            值为 A[i]+B[j]A[i]+B[j] 出现的次数。
            遍历到 C[k]+D[l] 时，如果 -(C[k]+D[l])−(C[k]+D[l]) 出现在哈希映射中，
            那么将 -(C[k]+D[l])−(C[k]+D[l]) 对应的值累加进答案中。
            O(N^2)'''
        def partition():
            res = 0
            dict_ab = {}
            for i in range(len(A)):
                for j in range(len(B)):
                    if A[i]+ B[j] in dict_ab:
                        dict_ab[A[i]+B[j]] += 1
                    else: dict_ab[A[i]+B[j]] = 1
            for k in range(len(C)):
                for l in range(len(D)):
                    if -(C[k]+D[l]) in dict_ab:
                        res += dict_ab[-(C[k]+D[l])]
            return res

        return partition()



# @lc code=end

