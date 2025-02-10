class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class LinkedList():
    
    def __init__(self):
        self.head = None
    
    def insert(self,val: int):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            temp.next.prev = temp
    
    def update(self, val: list):
        temp = self.head
        index = 1
        while index != val[0]:
            temp = temp.next
            index += 1
        if temp.prev is not None:
            temp.prev.val += (val[1]-1)
        if temp.next is not None:
            temp.next.val +=(temp.val - val[1])
        temp.val = 0
    
    def val(self, w: int):
        temp = self.head
        index = 1
        while index != w:
            temp = temp.next
            index += 1
        return temp.val


NofWire = int(input())

birds = list(map(int, input().split()))

NofShot = int(input())

wire = LinkedList()

for i in range(NofWire):
    wire.insert(birds[i])
    


for i in range(NofShot):
    
    a = list(map(int, input().split()))
    
    wire.update(a)

for i in range(1, NofWire+1):
    print(wire.val(i), end = "\n")
    

