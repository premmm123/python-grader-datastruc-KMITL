class LinkedList:
    class Node:
        def __init__(self, data, next=None):
            self.data = data
            if next is None:
                self.next = None
            else:
                self.next = next

        def __str__(self):
            return str(self.data)

    def __init__(self, head=None):
        if head == None:
            self.head = self.tail = None
            self.size = 0
        else:
            self.head = head
            t = self.head
            self.size = 1
            while t.next != None:
                t = t.next
                self.size += 1
            self.tail = t

    def __str__(self):
        s = "Linked data : "
        p = self.head
        while p != None:
            s += str(p.data) + ' '
            p = p.next
        return s

    def __len__(self):
        return self.size

    def append(self, data):
        p = self.Node(data)
        if self.head == None:
            self.head = self.tail = p
        else:
            t = self.tail
            t.next = p
            self.tail = p
        self.size += 1

    def removeHead(self):
        if self.head == None:
            return
        if self.head.next == None:
            p = self.head
            self.head = None
        else:
            p = self.head
            self.head = self.head.next
        self.size -= 1
        return p.data

    def isEmpty(self):
        return self.size == 0

    def nodeAt(self, i):
        p = self.head
        for j in range(i):
            p = p.next
        return p

    def sort(self):
        if self.isEmpty() or self.size == 1:
            return
        n = self.size
        for i in range(n):
            for i in range(n-1):
                a = self.nodeAt(i)
                b = self.nodeAt(i+1)
                if b.data < a.data:
                    # swap
                    c = b.next
                    if i == 0:
                        b.next = a
                        a.next = c
                        self.head = b
                    else:
                        prev = self.nodeAt(i-1)
                        prev.next = b
                        a.next = c
                        b.next = a

    def mean(self):
        mean = 0
        p = self.head
        while p != None:
            mean += p.data
            p = p.next
        return mean/self.size

    def median(self):
        if self.isEmpty():
            return
        n = self.size
        if n % 2 == 1:
            return self.nodeAt(n//2).data
        else:
            return (self.nodeAt(n//2).data + self.nodeAt((n//2)-1).data)/2


inputlist = [int(e) for e in input('Enter numbers : ').split()]
l = LinkedList()
for i in inputlist:
    l.append(i)
print("Output :")
l.sort()
print(l)
print('Amount of data =', len(l))
print("Mean = %.2f" % l.mean())
print("Median = %.2f" % l.median())
