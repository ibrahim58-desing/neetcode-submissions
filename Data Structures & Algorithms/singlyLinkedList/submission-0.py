class ListNode:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node


class LinkedList:
    def __init__(self):
        self.head = ListNode(-1)   # Dummy node
        self.tail = self.head

    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0

        while curr:
            if i == index:
                return curr.val

            i += 1
            curr = curr.next

        return -1

    def insertHead(self, val: int) -> None:
        newNode = ListNode(val)

        newNode.next = self.head.next
        self.head.next = newNode

        if self.tail == self.head:
            self.tail = newNode

    def insertTail(self, val: int) -> None:
        newNode = ListNode(val)

        self.tail.next = newNode
        self.tail = newNode

    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head

        while i < index and curr.next:
            i += 1
            curr = curr.next

        # curr is the node BEFORE the node to remove
        if curr.next:
            if curr.next == self.tail:
                self.tail = curr

            curr.next = curr.next.next
            return True

        return False

    def getValues(self) -> list[int]:
        curr = self.head.next
        arr = []

        while curr:
            arr.append(curr.val)
            curr = curr.next

        return arr