# @before-stub-for-debug-begin
from python3problem118 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#
# https://leetcode-cn.com/problems/pascals-triangle/description/
#
# algorithms
# Easy (67.91%)
# Likes:    407
# Dislikes: 0
# Total Accepted:    129.2K
# Total Submissions: 187.6K
# Testcase Example:  '5'
#
# 给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
# 
# 
# 
# 在杨辉三角中，每个数是它左上方和右上方的数的和。
# 
# 示例:
# 
# 输入: 5
# 输出:
# [
# ⁠    [1],
# ⁠   [1,1],
# ⁠  [1,2,1],
# ⁠ [1,3,3,1],
# ⁠[1,4,6,4,1]
# ]
# 
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            row = [1] # 开头的1
            for j in range(i-1):
                row.append(res[i-1][j] + res[i-1][j+1])

            if i != 0: row.append(1) # 末尾的1
            res.append(row[:])

        return res

# @lc code=end

