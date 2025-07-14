from operator import index


class ListNode:
    def __init__(self, val: int):
        self.val: int = val # 节点值
        self.next: ListNode | None = None # 指向下一节点的引用


# 初始化链表 1 -> 3 -> 2 -> 5 -> 4
n0 = ListNode(1)
n1 = ListNode(3)
n2 = ListNode(2)
n3 = ListNode(5)
n4 = ListNode(4)
n0.next = n1
n1.next = n2
n2.next = n3
n3.next = n4
# 通常将头节点作为链表代称，上述链表可称链表n0

# 插入节点 O(1)
def insert(n0: ListNode, P: ListNode):
    """在链表的节点 n0 之后插入节点 P"""
    n1 = n0.next
    n0.next = P
    P.next = n1

# 删除节点O(1)
def remove(n0: ListNode):
    """删除链表的节点 n0 之后的首个节点"""
    if not n0.next:
        return
    n0.next = n0.next.next

# 访问节点 O(n)
def access(head, index) -> ListNode | None:
    for _ in range(index):
        if not head:
            return None
        head = head.next
    return head

# 查找节点 O(n)
def find(head, target):
    """在链表中查找值为 target 的首个节点，返回其索引"""
    index = 0
    while head:
        if head.val == target:
            return index
        head = head.next
        index += 1
    return -1

class DoubleListNode:
    """双向链表节点类"""
    def __init__(self, val: int):
        self.val: int = val
        self.prev: DoubleListNode | None = None
        self.next: DoubleListNode | None = None
        