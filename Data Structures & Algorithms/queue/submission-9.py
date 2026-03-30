class ListNode:
    def __init__(self, val = None, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev

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
        self.addelement(value, self.dummy_tail, self.dummy_tail.prev)
        

    def appendleft(self, value: int) -> None:
        self.addelement(value, self.dummy_head.next, self.dummy_head)
        

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        return self.popelement(self.dummy_tail.prev)
        

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        return self.popelement(self.dummy_head.next)
    
    def popelement(self, element: ListNode):
        cur = element
        cur.prev.next = cur.next
        cur.next.prev = cur.prev
        return cur.val
    
    def addelement(self, val, next = ListNode, prev = ListNode):
        cur = ListNode(val, next, prev)
        next.prev = cur
        prev.next = cur

        
