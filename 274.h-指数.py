#
# @lc app=leetcode.cn id=274 lang=python3
#
# [274] H 指数
#
# https://leetcode-cn.com/problems/h-index/description/
#
# algorithms
# Medium (38.75%)
# Likes:    108
# Dislikes: 0
# Total Accepted:    19.3K
# Total Submissions: 49.7K
# Testcase Example:  '[3,0,6,1,5]'
#
# 给定一位研究者论文被引用次数的数组（被引用次数是非负整数）。编写一个方法，计算出研究者的 h 指数。
# 
# h 指数的定义：h 代表“高引用次数”（high citations），一名科研人员的 h 指数是指他（她）的 （N 篇论文中）总共有 h
# 篇论文分别被引用了至少 h 次。且其余的 N - h 篇论文每篇被引用次数 不超过 h 次。
# 
# 例如：某人的 h 指数是 20，这表示他已发表的论文中，每篇被引用了至少 20 次的论文总共有 20 篇。
# 
# 
# 
# 示例：
# 
# 
# 输入：citations = [3,0,6,1,5]
# 输出：3 
# 解释：给定数组表示研究者总共有 5 篇论文，每篇论文相应的被引用了 3, 0, 6, 1, 5 次。
# 由于研究者有 3 篇论文每篇 至少 被引用了 3 次，其余两篇论文每篇被引用 不多于 3 次，所以她的 h 指数是 3。
# 
# 
# 
# 提示：如果 h 有多种可能的值，h 指数是其中最大的那个。
# 
#

# @lc code=start
# 思路1: 排序 citations[i]>i+1 最后一个i，h=i+1   O(nlogn)
# 思路2: 计数：引用量 O(n)
import random
class Solution:
    #def hIndex(self, citations: List[int]) -> int:
    def hIndex(self, citations):

        # 改进版快排，由大到小
        def quickSort(l, r):
            if l >= r: return # 到达边界条件
            
            k = citations[random.choice(range(l, r+1))] # 随机选择哨兵
            i = l
            j = r

            while i <= j:
                while citations[i] > k: i += 1
                while citations[j] < k: j -= 1
                if i <= j: #！！！！！！等于的时候 主要是为了 i++ j--
                    tmp = citations[i]
                    citations[i] = citations[j]
                    citations[j] = tmp
                    i += 1
                    j -= 1
            
            quickSort(l, j) # j ！！！
            quickSort(i, r) # i ！！！ （两边再快排有交叉）
            

        def h_sort():
            res = 0
            quickSort(0, len(citations)-1)
            for i in range(len(citations)):
                if citations[i]>=i+1:
                    res += 1
                else:break
            return res

        def h_count():
            
            # h 不会超过 n
            n = len(citations)
            cnt = [0] * (n+1)
            # 引用量为0 - n(包含>n)的论文数
            for i in citations:
                if i > n:
                    cnt[n] += 1
                else:
                    cnt[i] += 1
            
            # 引用量至少为0 - n(包含>n)的论文数
            if cnt[n] >= n: return n
            for i in range(1, n+1):
                cnt[n-i] = cnt[n-i+1]+cnt[n-i]
                if cnt[n-i] >= n-i: return n-i

        return h_count()
#s= Solution()
#s.hIndex([0,1,0])
# @lc code=end

