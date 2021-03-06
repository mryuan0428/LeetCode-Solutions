#
# @lc app=leetcode.cn id=1046 lang=python3
#
# [1046] 最后一块石头的重量
#
# https://leetcode-cn.com/problems/last-stone-weight/description/
#
# algorithms
# Easy (65.91%)
# Likes:    152
# Dislikes: 0
# Total Accepted:    54.6K
# Total Submissions: 82.9K
# Testcase Example:  '[2,7,4,1,8,1]'
#
# 有一堆石头，每块石头的重量都是正整数。
# 
# 每一回合，从中选出两块 最重的 石头，然后将它们一起粉碎。假设石头的重量分别为 x 和 y，且 x <= y。那么粉碎的可能结果如下：
# 
# 
# 如果 x == y，那么两块石头都会被完全粉碎；
# 如果 x != y，那么重量为 x 的石头将会完全粉碎，而重量为 y 的石头新重量为 y-x。
# 
# 
# 最后，最多只会剩下一块石头。返回此石头的重量。如果没有石头剩下，就返回 0。
# 
# 
# 
# 示例：
# 
# 输入：[2,7,4,1,8,1]
# 输出：1
# 解释：
# 先选出 7 和 8，得到 1，所以数组转换为 [2,4,1,1,1]，
# 再选出 2 和 4，得到 2，所以数组转换为 [2,1,1,1]，
# 接着是 2 和 1，得到 1，所以数组转换为 [1,1,1]，
# 最后选出 1 和 1，得到 0，最终数组转换为 [1]，这就是最后剩下那块石头的重量。
# 
# 
# 
# 提示：
# 
# 
# 1 <= stones.length <= 30
# 1 <= stones[i] <= 1000
# 
# 
#
# 堆排序
# @lc code=start
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        size = len(stones)
        if size == 1: return stones[0]

        stones_heap = self.getMaxHeap(stones, size)
        while size > 1:
            s_1 = stones_heap[0]
            size -= 1
            stones_heap[0] = stones_heap[size]
            self.maxHeapify(stones_heap, 0, size)
            
            s_2 = stones_heap[0]

            if s_1 == s_2:
                size -= 1
                if size == 0: return 0
                stones_heap[0] = stones_heap[size]
                self.maxHeapify(stones_heap, 0, size)
            else: 
                stones_heap[0] = s_1 - s_2
                self.maxHeapify(stones_heap, 0, size)
        return stones_heap[0]

    def getMaxHeap(self, stones, size):
        for j in range(len(stones)//2, 0, -1):
            i = j - 1
            self.maxHeapify(stones, i, size)
        return stones


    def maxHeapify(self, stones, i, size):
        largest = i
        if(2*i+1<size and stones[2*i+1]>stones[i]):
            largest = 2*i+1
        if(2*i+2<size and stones[2*i+2]>stones[largest]):
            largest = 2*i+2
        if largest != i:
            tmp = stones[i]
            stones[i] = stones[largest]
            stones[largest] = tmp
            self.maxHeapify(stones, largest, size)


# @lc code=end

