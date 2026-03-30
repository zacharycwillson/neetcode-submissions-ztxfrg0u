class listNode():
    def __init__(self, val = None):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.linked_list = listNode()
        self.tail = None

    
    def get(self, index: int) -> int:
        cur = self.linked_list.next
        cur_index = 0
        while cur and cur_index < index:
            cur = cur.next
            cur_index += 1
        if cur:
            return cur.val
        return -1

    def insertHead(self, val: int) -> None:
        cur = listNode(val)
        if self.linked_list.next:
            cur.next = self.linked_list.next
        else:
            self.tail = cur
        self.linked_list.next = cur
        

    def insertTail(self, val: int) -> None:
        cur = listNode(val)
        if not self.linked_list.next:
            self.linked_list.next = cur
        else:
            self.tail.next = cur
        self.tail = cur
        

    def remove(self, index: int) -> bool:
        cur = self.linked_list.next
        prev = self.linked_list
        index_count = 0
        while cur:
            if index_count == index:
                if not cur.next:
                    self.tail = prev
                    self.tail.next = None
                else:
                    prev.next = cur.next
                return True
            prev = cur
            cur = cur.next
            index_count += 1
        return False

        

    def getValues(self) -> List[int]:
        res = []
        cur = self.linked_list.next
        while cur:
            res.append(cur.val)
            cur = cur.next
        return res
        
