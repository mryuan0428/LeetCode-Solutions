#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU缓存机制
#
# https://leetcode-cn.com/problems/lru-cache/description/
#
# algorithms
# Medium (50.73%)
# Likes:    983
# Dislikes: 0
# Total Accepted:    110.2K
# Total Submissions: 215.8K
# Testcase Example:  '["LRUCache","put","put","get","put","get","put","get","get","get"]\n' +
# '[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]'
#
# 运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制 。
# 
# 
# 
# 实现 LRUCache 类：
# 
# 
# LRUCache(int capacity) 以正整数作为容量 capacity 初始化 LRU 缓存
# int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
# void put(int key, int value)
# 如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该组「关键字-值」。当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。
# 
# 
# 
# 
# 
# 
# 进阶：你是否可以在 O(1) 时间复杂度内完成这两种操作？
# 
# 
# 
# 示例：
# 
# 
# 输入
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# 输出
# [null, null, null, 1, null, -1, null, -1, 3, 4]
# 
# 解释
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // 缓存是 {1=1}
# lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
# lRUCache.get(1);    // 返回 1
# lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
# lRUCache.get(2);    // 返回 -1 (未找到)
# lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
# lRUCache.get(1);    // 返回 -1 (未找到)
# lRUCache.get(3);    // 返回 3
# lRUCache.get(4);    // 返回 4
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 0 
# 0 
# 最多调用 3 * 10^4 次 get 和 put
# 
# 
#

# @lc code=start
"""
所谓LRU缓存，根本的难点在于记录最久被使用的键值对，这就设计到排序的问题，
在python中，天生具备排序功能的字典就是OrderedDict。
注意到，记录最久未被使用的键值对的充要条件是将每一次put/get的键值对都定义为
最近访问，那么最久未被使用的键值对自然就会排到最后。
如果你深入python OrderDict的底层实现，就会知道它的本质是个双向链表+字典。
它内置支持了
1. move_to_end来重排链表顺序，它可以让我们将最近访问的键值对放到最后面
2. popitem来弹出键值对，它既可以弹出最近的，也可以弹出最远的，弹出最远的就是我们要的操作。

from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity  # cache的容量
        self.visited = OrderedDict()  # python内置的OrderDict具备排序的功能
    def get(self, key: int) -> int:
        if key not in self.visited:
            return -1
        self.visited.move_to_end(key)  # 最近访问的放到链表最后，维护好顺序
        return self.visited[key]
    def put(self, key: int, value: int) -> None:
        if key not in self.visited and len(self.visited) == self.capacity:
              # last=False时，按照FIFO顺序弹出键值对
              # 因为我们将最近访问的放到最后，所以最远访问的就是最前的，也就是最first的，故要用FIFO顺序
            self.visited.popitem(last=False)
        self.visited[key]=value
        self.visited.move_to_end(key)    # 最近访问的放到链表最后，维护好顺序
"""


#自己实现 哈希表+双向链表，哈希表可以用python自带的字典{}
#get好写，哈希表就是实现O(1)get
# 将最近访问的放到最后，所以最远访问的就是最前的
class BiListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        self.head = BiListNode()
        self.tail = BiListNode()
        
        self.head.next = self.tail
        self.tail.prev = self.head

    def move_to_end(self, node):
        # 考察双向链表节点的移动：
        # 移出(需要判断，可能是新节点)：
        if node.prev and node.next:
            node.prev.next = node.next
            node.next.prev = node.prev

        # 移入：
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node

    def remove_lrunode(self):
        # 移出头上lru的节点
        self.head.next = self.head.next.next
        self.head.next.prev = self.head

    def get(self, key: int) -> int:
        # 若存在，则移到尾端，并返回
        if key in self.hashmap:
            self.move_to_end(self.hashmap[key])
            return self.hashmap[key].value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.hashmap[key].value = value
            self.move_to_end(self.hashmap[key])
        else:
            if len(self.hashmap) >= self.capacity:
                self.hashmap.pop(self.head.next.key)
                self.remove_lrunode()
                new_node = BiListNode(key, value)
                self.hashmap[key] = new_node
                self.move_to_end(new_node)
            else:
                new_node = BiListNode(key, value)
                self.hashmap[key] = new_node
                self.move_to_end(new_node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

