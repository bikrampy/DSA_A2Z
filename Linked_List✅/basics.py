class Node:
    def __init__(self, data= None, next= None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_beg(self, data):
        node = Node(data, self.head)
        self.head = node
    
    def insert_end(self, data):
        if self.head is None:
            node = Node(data, self.head)
            self.head = node
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)
    
    def insert_val(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_end(data)

    def print(self):
        if self.head is None:
            print("LL is Empty.")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + "--->"
            itr = itr.next
        print(llstr)
    
    def getLength(self):
        itr = self.head
        length = 0
        while itr:
            length += 1
            itr = itr.next
        print(length)
    
    def removeAt(self, index):
        if index < 0 and index >= self.length:
            raise Exception("Invalid Input")
        if index == 0:
            self.head = self.head.next
        count = 0
        itr = self.head
        while itr:
            if count == index -1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1
    
    def insertAt(self, index, data):
        if index < 0 and index > self.length:
            raise Exception("Invalid Input")
        if index == 0:
            self.insert_beg(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
            itr = itr.next
            count += 1
    
    def search(self, data):
        count = 0
        itr = self.head
        while itr:
            if itr.data == data:
                return f'Element Found at Index {count}.'
            itr = itr.next
            count += 1
        return 'Element not found.'


llist = LinkedList()
llist.insert_beg(3)
llist.insert_beg(2)
llist.insert_end(5)
llist.insert_end(4)
llist.insert_beg(9)
llist.print()
llist.getLength()
llist.removeAt(2)
llist.print()
llist.insertAt(4, 78)
llist.print()
print(llist.search(4))