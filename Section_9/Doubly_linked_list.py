class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def createList(self, arr):
        start = self.head
        n = self.size = len(arr)

        temp = start
        i = 0

        while (i < n):
            newNode = Node(arr[i])
            if (i == 0):
                start = newNode
                temp = start
            else:
                temp.next = newNode
                newNode.prev = temp
                temp = temp.next
            i += 1
        self.head = start
        return start

    def printList(self):
        temp = self.head
        linked_list = ""
        while (temp):
            linked_list += (str(temp.data) + " ")
            temp = temp.next

        print(linked_list)

    def countList(self):
        temp = self.head

    # we will consider that the index begin at 1
    def insertAtLocation(self, value, index):
        temp = self.head
        count = self.size

        # index is 6, count is 5, valid
        # index is 7, count is 5,
        if (count + 1 < index):
            return temp

        newNode = Node(value)

        if (index == 1):
            newNode.next = temp
            temp.prev = newNode
            self.head = newNode
            self.size += 1
            return self.head

        if (index == count + 1):
            while (temp.next is not None):
                temp = temp.next

            temp.next = newNode
            newNode.prev = temp
            self.size += 1
            return self.head

        i = 1
        while (i < index - 1):
            temp = temp.next
            i += 1

        newNode.next = temp.next
        newNode.prev = temp

        temp.next.prev = newNode
        temp.next = newNode

        # nodeAtTarget = temp.next
        #
        # newNode.next = nodeAtTarget
        # nodeAtTarget.prev = newNode
        #
        # temp.next = newNode
        # newNode.prev = temp
        self.size += 1
        return self.head

    def deleteAtLocation(self, index):
        temp = self.head
        count = self.size

        if index > count:
            return temp

        if index == 1:
            self.head = self.head.next
            return self.head

        i = 1

        if index == count:
            while i < count-1:
                i += 1
                temp = temp.next

            temp.next = None
            return self.head

        i = 1
        while i < index - 1:
            i += 1
            temp = temp.next

        deleted_node = temp.next

        deleted_node.next.prev = temp
        temp.next = deleted_node.next



arr = [1, 2, 3, 4, 5]

list = LinkedList()

list.createList(arr)

list.insertAtLocation(6, 7)

list.deleteAtLocation(6)

list.printList()
