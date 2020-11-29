#
# @lc app=leetcode.cn id=976 lang=python3
#
# [976] 三角形的最大周长
#
# https://leetcode-cn.com/problems/largest-perimeter-triangle/description/
#
# algorithms
# Easy (56.01%)
# Likes:    125
# Dislikes: 0
# Total Accepted:    41.4K
# Total Submissions: 69.4K
# Testcase Example:  '[2,1,2]'
#
# 给定由一些正数（代表长度）组成的数组 A，返回由其中三个长度组成的、面积不为零的三角形的最大周长。
# 
# 如果不能形成任何面积不为零的三角形，返回 0。
# 
# 
# 
# 
# 
# 
# 示例 1：
# 
# 输入：[2,1,2]
# 输出：5
# 
# 
# 示例 2：
# 
# 输入：[1,2,1]
# 输出：0
# 
# 
# 示例 3：
# 
# 输入：[3,2,3,4]
# 输出：10
# 
# 
# 示例 4：
# 
# 输入：[3,6,2,3]
# 输出：8
# 
# 
# 
# 
# 提示：
# 
# 
# 3 <= A.length <= 10000
# 1 <= A[i] <= 10^6
# 
# 
#

# @lc code=start
class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        def quickSort(l, r):
            while l < r:
                x = l
                y = r
                z = A[(x+y)//2]

                while x < y:
                    while A[x] > z: x += 1
                    while A[y] < z: y -= 1
                    if x <= y:
                        tmp = A[x]
                        A[x] = A[y]
                        A[y] = tmp
                        x += 1
                        y -= 1
                quickSort(l, y)
                l = x
        
        n = len(A)
        #quickSort(0, n-1)
        #A.sort(reverse=True)
        A = sorted(A, reverse=True)

        for i in range(n-2):
            t = A[i+1] + A[i+2]
            if A[i] < t:
                return A[i] + t
        return 0
        
# @lc code=end

