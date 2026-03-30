class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.array = [None] * capacity
        self.length = 0



    def get(self, i: int) -> int:
        return self.array[i]


    def set(self, i: int, n: int) -> None:
        self.array[i] = n


    def pushback(self, n: int) -> None:
        if self.length >= self.capacity:
            self.resize()
        self.set(self.length, n)
        self.length += 1


    def popback(self) -> int:
        res = self.array[self.length - 1]
        self.array[self.length - 1] = None
        self.length -= 1
        return res
 

    def resize(self) -> None:
        self.capacity = 2 * self.capacity
        new_array = [None] * self.capacity
        for i in range(self.length):
            new_array[i] = self.array[i]
        self.array = new_array
        


    def getSize(self) -> int:
        return self.length
        
    
    def getCapacity(self) -> int:
        return self.capacity
