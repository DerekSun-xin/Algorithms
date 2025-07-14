'''Iteration
for: for循环适用于知道迭代次数
while: 灵活，自由设计条件变量初始化和更新操作
'''

''' 1 + 4 + 10 '''
def while_loop_ii(n: int) -> int:
    res = 0
    i = 1
    while i <= n:
        res += i
        i += 1
        i *= 2
    return res

