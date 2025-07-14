# 列表list无需使用者考虑容量限制问题
# 列表基于数组或者链表实现
# 列表和动态数组(dynamic array)为等同概念
from bisect import insort_right
from itertools import count

# 1. 初始化列表
nums1: list[int] = []
nums2: list[int] = [1, 2, 3, 4, 5]
nums3: list[int] = list(range(10))

# 2.访问元素 O(1)
num: int = nums2[0]
nums2[1] = 0 # 将索引1处的元素更新为0

# 3. 插入与删除元素
# 在list尾部添加元素:O(1)
# 插入和删除元素: O(n)
nums2.clear() # 清空列表

# 在尾部添加元素 O(1)
nums1.append(1)

# 在中间插入元素 O(n)
nums2.insert(3, 6) # 在索引3处插入数字6

# 删除元素 O(n)
nums2.pop(3) # 删除索引3处的元素

# 拼接两个列表
nums: list[int] = []
nums  += nums1  # 将列表nums1拼接到nums之后

# 列表排序
nums.sort() # 从小到大排列

class MyList:
    def __init__(self):
        self._capacity: int = 10 # 列表容量
        self._arr: list[int] = [] # 数组(存储列表元素）
        self._size: int = 0 # 列表长度 （当前元素数量）
        self._extend_ratio: int = 2 # 列表扩容倍数

    def size(self) -> int:
        return self._size

    def capacity(self) -> int:
        return self._capacity

    def get(self, index: int) -> int:
        if index < 0 or index >= self._size:
            raise IndexError("index out of range")
        return self._arr[index]

    def set(self, num: int, index: int):
        """更新元素"""
        if index < 0 or index >= self._size:
            raise IndexError("index out of range")
        self._arr[index] = num

    def add(self, num: int):
        """在尾部添加元素"""
        # 元素数量超出容量时，触发扩容机制
        if self.size() == self.capacity():
            self.extend_capacity()
        self._arr[self.size()] = num
        self._size += 1

    def insert(self, num, index):
        """在中间插入元素"""
        if index < 0 or index > self.size():
            raise IndexError("index out of range")
        # 元素超出容量限制时，触发扩容机制
        if self.size() == self.capacity():
            self.extend_capacity()
        for j in range(self.size() - 1, index - 1, -1 ):
            self._arr[j + 1] = self._arr[j]
        self._arr[index] = num
        self._size += 1
    
    def remove(self, index: int) -> int:
        if index < 0 or index > self.size() - 1:
            raise IndexError("Index Out of range")
        num = self._arr[index]
        for i in range(index, self.size() - 1):
            self._arr[i] = self._arr[i + 1]
        self._size -= 1
        return num

    def extend_capacity(self):
        self._arr = self._arr + (self._extend_ratio - 1) * self.capacity() * [0]
        self._capacity = len(self._arr)

    def to_array(self) -> list[int]:
        """返回有效长度的列表"""
        return self._arr[:self.size()]



