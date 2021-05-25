from node import Node


class LinkedList:
    def __init__(self):
        self.head = None
        self.contains = None


    def append_node(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
            return

        temporary_node = self.head

        while temporary_node.next is not None:
            temporary_node = temporary_node.next

        temporary_node.next = node


    def add_to_beginning(self, data):
        node = Node(data)

        node.next = self.head
        self.head = node


    def contains_node(self, value):
        node = self.head
        node_id = 1
        results = []

        while node is not None:
            if node.contains(value):
                results.append(node_id)
            node = node.next
            node_id = node_id + 1

        if results:
            print(results)
        else:
            print("Not Found")
        return results