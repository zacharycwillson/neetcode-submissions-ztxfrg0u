class ListNode:

    def __init__(self, val: int, next = None):
        self.val = val
        self.next = next

        
class LinkedList:
    
    def __init__(self):
        self.dummy_head = ListNode(None)
        self.tail = self.dummy_head

    
    def get(self, index: int) -> int:
        cur = self.dummy_head.next
        cur_index = 0
        while cur and cur_index < index:
            cur = cur.next
            cur_index += 1
        if cur:
            return cur.val
        return -1
        

    def insertHead(self, val: int) -> None:
        new_head = ListNode(val, self.dummy_head.next)
        self.dummy_head.next = new_head
        if self.tail == self.dummy_head:
            self.tail = new_head
        

    def insertTail(self, val: int) -> None:
        new_tail = ListNode(val)
        self.tail.next = new_tail
        self.tail = new_tail

        

    def remove(self, index: int) -> bool:
        cur = self.dummy_head.next
        prev = self.dummy_head
        cur_index = 0
        while cur and cur_index < index:
            prev = cur
            cur = cur.next
            cur_index += 1
        if cur:
            prev.next = cur.next
            if cur == self.tail:
                self.tail = prev
            return True
        return False

        

    def getValues(self) -> List[int]:
        res = []
        cur = self.dummy_head.next
        while cur:
            res.append(cur.val)
            cur = cur.next
        return res
        
