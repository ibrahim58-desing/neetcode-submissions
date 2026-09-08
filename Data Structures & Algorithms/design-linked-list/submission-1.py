class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class MyLinkedList:

    def __init__(self):
        self.head = ListNode(-1)
        self.tail = ListNode(-1)

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0

        while curr != self.tail:
            if i == index:
                return curr.value

            i += 1
            curr = curr.next

        return -1

    def addAtHead(self, val: int) -> None:
        newNode = ListNode(val)

        newNode.next = self.head.next
        newNode.prev = self.head

        self.head.next.prev = newNode
        self.head.next = newNode

    def addAtTail(self, val: int) -> None:
        newNode = ListNode(val)

        newNode.next = self.tail
        newNode.prev = self.tail.prev

        self.tail.prev.next = newNode
        self.tail.prev = newNode

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            return

        curr = self.head.next
        i = 0

        while i < index and curr != self.tail:
            i += 1
            curr = curr.next

        if i != index:
            return

        newNode = ListNode(val)

        newNode.next = curr
        newNode.prev = curr.prev

        curr.prev.next = newNode
        curr.prev = newNode

    def deleteAtIndex(self, index: int) -> None:
        if index < 0:
            return

        curr = self.head.next
        i = 0

        while i < index and curr != self.tail:
            i += 1
            curr = curr.next

        if curr == self.tail:
            return

        curr.prev.next = curr.next
        curr.next.prev = curr.prev