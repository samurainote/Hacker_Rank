
"""
tree
"""

class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def preOrder(root):
    #Write your code here
    if root != None:
        print(root.data, end=" ")
        preOrder(root.left)
        preOrder(root.right)

def getHeight(self, root):
    #Write your code here
    left_Height = 0
    right_Height = 0
    if root.left:
        left_Height = self.getHeight(root.left) + 1
    if root.right:
        right_Height = self.getHeight(root.right) + 1

    if left_Height > right_Height:
        return left_Height
    else:
        return right_Height
