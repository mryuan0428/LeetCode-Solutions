#
# @lc app=leetcode.cn id=1318 lang=python3
#
# [1318] 或运算的最小翻转次数
#
# https://leetcode-cn.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/description/
#
# algorithms
# Medium (63.63%)
# Likes:    20
# Dislikes: 0
# Total Accepted:    3.9K
# Total Submissions: 6.1K
# Testcase Example:  '2\n6\n5'
#
# 给你三个正整数 a、b 和 c。
# 
# 你可以对 a 和 b 的二进制表示进行位翻转操作，返回能够使按位或运算   a OR b == c  成立的最小翻转次数。
# 
# 「位翻转操作」是指将一个数的二进制表示任何单个位上的 1 变成 0 或者 0 变成 1 。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：a = 2, b = 6, c = 5
# 输出：3
# 解释：翻转后 a = 1 , b = 4 , c = 5 使得 a OR b == c
# 
# 示例 2：
# 
# 输入：a = 4, b = 2, c = 7
# 输出：1
# 
# 
# 示例 3：
# 
# 输入：a = 1, b = 2, c = 3
# 输出：0
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= a <= 10^9
# 1 <= b <= 10^9
# 1 <= c <= 10^9
# 
# 
#

# @lc code=start
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        cnt = 0
        while a or b or c:
            if (a&1) | (b&1) != c&1:
                if c & 1: 
                    cnt += 1
                    
                else:
                    cnt += a&1
                    cnt += b&1
            a = a >> 1
            b = b >> 1
            c = c >> 1
        return cnt


# @lc code=end

