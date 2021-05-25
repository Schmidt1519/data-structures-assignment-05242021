class BSTNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


    def insert_node(self, data):
        if not self.data:
            self.data = data
            return

        if self.data == data:
            return

        if data < self.data:
            if self.left:
                self.left.insert(data)
                return
            self.left = BSTNode(data)
            return

        if self.right:
            self.right.insert(data)
            return
        self.right = BSTNode(data)


    # def insert_node(root, data):
    #     if root is None:
    #         return BSTNode(data)
    #     else:
    #         if root.data == data:
    #             return root
    #         elif root.data < data:
    #             root.right = insert_node(root.right, data)
    #         else:
    #             root.left = insert_node(root.left, data)
    #     return root


    def search_for_node(self, data):
        if self is None or self.data == data:
            return self

        if self.data < data:
            return search_for_node(self.right, data)

        return search_for_node(self.left, data)

