# 初始化数组(array)
# 初始化方式：无初始值，给定初始值 （未指定初始值，数组元素初始化为0）
import random

arr: list[int] = [0] * 10
print(arr)
nums:list[int] [1, 2, 3, 4, 5]

# 访问元素 O(1)
def random_access(nums:list[int]) -> int:
    random_index = random.randint(0, len(nums) - 1)
    randon_num = nums[random_index]
    return randon_num

# O(n)
def insert(nums: list[int], num:int, index: int):
    '''在数组索引index处插入元素num'''
    # 把索引index以及之后的元素向后移动一位
    for i in range(len(nums) - 1, index, -1):
        nums[i] = nums[i - 1]
    nums[index] = num

# O(n)
def remove(nums, index):
    for i in range(index, len(nums) - 1):
        nums[i] = nums[i + 1]
# O(n)
def find(nums, target) -> int:
    """在数组中查找指定元素"""
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1

#O(n)
def extend(nums, enlarge) -> list[int]:
    res = [0] * (len(nums) + enlarge)
    for i in range(len(nums)):
        res[i] = nums[i]
    return res; 