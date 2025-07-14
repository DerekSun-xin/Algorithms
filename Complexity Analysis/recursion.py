'''1 + 2 + 3 + ... + n'''
from inspect import stack


def recur(n: int) -> int:
    if n == 0:
        return 0
    return n + recur(n - 1)

'''
尾递归：求和操作在递中执行，归只需层层返回。部分编译器可优化尾递归，使之在空间效率上和迭代相当
'''
def tail_recur(n ,res):
    if n == 0:
        return res
    return tail_recur(n - 1, res + n)

# 求n，n为斐波那契数列第n个数字
def fib(n:int) -> int:
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)

# 使用迭代模拟递归
def for_loop_recur(n:int) -> int:
    stack = []
    res = 0
    # 递:
    for i in range(n, 0, -1):
        stack.append(i)
    # 归:
    while stack:
        cur = stack.pop()
        print(cur)
        res += cur

def logarithmic(n:int) -> int:
    '''对数阶'''
    count = 0 # 每轮缩减一半，缩减多少轮
    while n > 1:
        n = n/2
        count += 1
    return count

def log_recur(n:int) -> int:
    '''对数阶'''
    if n <= 1:
        return 0
    return log_recur(n/2) + 1

def factorial_recur(n:int) -> int:
    '''阶乘阶（递归) '''
    if n == 0:
        return 1
    count = 0
    for i in range(n):
        count += factorial_recur(n - 1)
    return count;

print(factorial_recur(3))