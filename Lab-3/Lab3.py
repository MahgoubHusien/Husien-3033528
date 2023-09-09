class SLList:
    class IntNode:
        def __init__(self, item, next_node):
            self.item = item  # int
            self.next = next_node  # IntNode

    def __init__(self):
        self.first = None  # initialize an empty list
        self.length = 0

    def addFirst(self, item):
        self.first = self.IntNode(item, self.first)
        self.length += 1

    def insert(self, item, position):
        iterate = self.first
        item = self.IntNode(item, iterate)
        if position == 0 or iterate == None:
            item.next = iterate
            self.first = item
        elif position <= self.length and position >= 1:
            for step in range(position-1):
                iterate = iterate.next
            item.next = iterate.next
            iterate.next = item
        else:
            raise IndexError("Index is not within list range")
        self.length += 1

    def get_entry(self, position):
        iterate = self.first
        if iterate == None:
            return
        if position <= self.length and position >= 0:
            for step in range(position-1):
                iterate = iterate.next
            return iterate.item

    def replicate(self):
        new_list = SLList()
        current = self.first
        while current:
            for entry in range(1, self.length+1):
                node = self.get_entry(entry)
                for num in range(node):
                    new_list.insert(node, num)
            break
        return new_list

    def reverse(self):
        if not self.first or not self.first.next:
            return
        previous = None
        current = self.first #3->2->1 3=current
        while current != None:
            nxt = current.next #2
            current.next = previous #3->None
            previous = current
            current = nxt
        self.first = previous

    def equals(self, anotherList):
        al = anotherList
        if self.length != al.length:
            return False
        if self.length == al.length:
            for num in range(self.length):
                if self.get_entry(num) != al.get_entry(num):
                    return False
        return True

    def pr(self):
        current = self.first
        while current:
            print(current.item)
            current = current.next

if __name__ == '__main__':
  L = SLList()
  L.addFirst(15)
  L.addFirst(10)
  L.addFirst(5)
  L.reverse()


  L_expect = SLList()
  L_expect.addFirst(5)
  L_expect.addFirst(10)
  L_expect.addFirst(15)

  if L.equals(L_expect):
    print("Two lists are equal, tests passed")
  else:
    print("Two lists are not equal, tests failed")
