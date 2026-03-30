class ListNode:
    def __init__(self, val: int = None, prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next

class Deque:
    
    def __init__(self):
        self.dummy_head = ListNode()
        self.dummy_tail = ListNode()
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head


    def isEmpty(self) -> bool:
        if self.dummy_head.next == self.dummy_tail:
            return True
        return False
        

    def append(self, value: int) -> None:
        self.addnode(value, self.dummy_tail.prev, self.dummy_tail)
        

    def appendleft(self, value: int) -> None:
        self.addnode(value, self.dummy_head, self.dummy_head.next)
        

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        return self.removenode(self.dummy_tail.prev)
        

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        return self.removenode(self.dummy_head.next)

    def addnode(self, val: int, prev: ListNode, next: ListNode):
        new_node = ListNode(val, prev, next)
        prev.next = new_node
        next.prev = new_node

    def removenode(self, node: ListNode):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        return node.val
