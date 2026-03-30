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
        prev = None
        index_count = 0
        if cur and not index:
            if not cur.next:
                self.linked_list.next = None
            else:
                self.linked_list.next = cur.next
            return True
        while cur:
            index_count += 1
            prev = cur
            cur = cur.next
            if index_count == index and cur:
                if not cur.next:
                    self.tail = prev
                    self.tail.next = None
                else:
                    prev.next = cur.next
                return True
        return False

        

    def getValues(self) -> List[int]:
        res = []
        cur = self.linked_list.next
        while cur:
            res.append(cur.val)
            cur = cur.next
        return res
        
