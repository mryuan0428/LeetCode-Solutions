#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#
# https://leetcode-cn.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (38.40%)
# Likes:    2931
# Dislikes: 0
# Total Accepted:    226.2K
# Total Submissions: 589.1K
# Testcase Example:  '[1,3]\n[2]'
#
# 给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。
# 
# 请你找出这两个正序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
# 
# 你可以假设 nums1 和 nums2 不会同时为空。
# 
# 示例 1:
# 
# nums1 = [1, 3]
# nums2 = [2]
# 
# 则中位数是 2.0
# 
# 
# 示例 2:
# 
# nums1 = [1, 2]
# nums2 = [3, 4]
# 
# 则中位数是 (2 + 3)/2 = 2.5
# 
# 
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #复杂度要求O(log(m + n))

        # 找两个排好序的数组的第k小的变种 ! ! !
        # 每次比较两数组第k/2个数，并删去小的前k/2个
        # k = k - k/2
        # 再继续删除直到k = 1
        l1 = len(nums1)
        l2 = len(nums2)
        if l1 == 0:
            return nums2[l2//2] if l2%2==1 else (nums2[l2//2-1]+nums2[l2//2])/2
        if l2 == 0:
            return nums1[l1//2] if l1%2==1 else (nums1[l1//2-1]+nums1[l1//2])/2 
        
        if (l1+l2)%2==1:
            return self.get_kth(nums1, nums2, ((l1+l2)//2+1), False)
        else:
            return self.get_kth(nums1, nums2, (l1+l2)//2, True) #返回两数的均值
    
    def get_kth(self, l1, l2, k, is_even):
        #若l1或l2为空
        if len(l1) == 0:
            if not is_even:
                return l2[k-1]
            else:
                return (l2[k-1] + l2[k]) / 2
        if len(l2) == 0:
            if not is_even:
                return l1[k-1]
            else:
                return (l1[k-1] + l1[k]) / 2
        
        #若k为1
        if k == 1:
            if not is_even:
                return min(l1[0], l2[0])
            else:
                return (min(l1[0], l2[0]) + self.get_kth(l1, l2, 2, False)) / 2
        
        p = min(k // 2, len(l1), len(l2))
        if l1[p-1] <= l2[p-1]:
            return self.get_kth(l1[p:], l2, k-p, is_even)
        else:
            return self.get_kth(l1, l2[p:], k-p, is_even)



# @lc code=end

