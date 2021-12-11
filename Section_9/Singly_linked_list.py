class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        linked_list = ""

        while temp:
            linked_list += (str(temp.data) + " ")
            temp = temp.next

        print(linked_list)

    def insertNode(self, value, position):
        target = Node(value)

        if position == 0:
            target.next = self.head
            self.head = target
            return

        position_counter = 1
        temp_node = self.head

        while position_counter != position:
            temp_node = temp_node.next
            if temp_node is None:
                print("cant insert out of list's range")
                return
            position_counter += 1

        previous_node = self.getPreviousNode(position)
        target.next = previous_node.next
        previous_node.next = target

    def getPreviousNode(self, position):
        position_counter = 1
        temp_node = self.head

        while position_counter < position:
            temp_node = temp_node.next
            position_counter += 1

        return temp_node

    def deleteNode(self, key):
        temp = self.head
        if temp is None:
            print("node not found")
            return

        if temp.data == key:
            target_node = self.head
            self.head = self.head.next
            target_node = None
            return

        while temp.next is not None and temp.next.data != key:
            temp = temp.next

        if temp.next is not None and temp.next.data == key:
            target_node = temp.next
            temp.next = target_node.next
            target_node.next = None


linked_list = LinkedList()
linked_list.head = Node(5)

second_node = Node(1)
third_node = Node(3)
fourth_node = Node(7)

linked_list.head.next = second_node
second_node.next = third_node
third_node.next = fourth_node

linked_list.printList()

linked_list.insertNode(10, 90)
linked_list.deleteNode(5)
linked_list.printList()
