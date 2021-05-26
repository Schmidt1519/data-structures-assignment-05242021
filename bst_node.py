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
                self.left.insert_node(data)
                return
            self.left = BSTNode(data)
            return

        if self.right:
            self.right.insert_node(data)
            return
        self.right = BSTNode(data)


    def search_for_node(self, value):
        if self.data == value:
            print(f'{value} is found.')
            return True

        if value < self.data:
            if self.left:
                return self.left.search_for_node(value)
            else:
                print(f'{value} is not found.')
                return False

        if value > self.data:
            if self.right:
                return self.right.search_for_node(value)
            else:
                print(f'{value} is not found.')
                return False


    def print_inorder(self):
        if self.left:
            self.left.print_inorder()
        print(self.data),
        if self.right:
            self.right.print_inorder()


    def print_preorder(self):
        print(self.data)
        if self.left:
            self.left.print_preorder()
        if self.right:
            self.right.print_preorder()