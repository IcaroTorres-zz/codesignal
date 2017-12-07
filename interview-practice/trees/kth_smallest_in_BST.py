'''Binary Search Tree script class to solve codefights interview practice Trees - "kthSmallestInBST"'''

# class code to test out of codefights
class BST(object):
    '''BST(value) -> Binary Search Tree Object {
    \t    self.value = value,
    \t    self.left = BST Object | None,
    \t    self.right = BST Object | None
    }
    A BST Object representing a Tree (or Sub-Tree)
    with a ".value" porperty and 2 Child BST Nodes
    ".left" and ".right" pointing to "None" as default'''

    def __init__(self, value=None):
        '''".value" = a value to be stored and compared on new insertion or removal'''
        self.value = value
        self.left = None
        self.right = None

    def tostring(self, identation=0):
        '''A simple display function to expose a BST from it\'s root to leafs'''
        spaces = '  ' * identation
        printable = '{"value":' + str(self.value)
        if self.left:
            printable += ',\n' + spaces + '"left": ' + \
                self.left.tostring(identation + 1) + '}'
        else:
            printable += ',\n' + spaces + '"left": None'
        if self.right:
            printable += ',\n' + spaces + '"right": ' + \
                self.right.tostring(identation + 1) + '}'
        else:
            printable += ',\n' + spaces + '"right": None'

        return printable

    def find(self, value):
        '''find(value) -> BST with given value | None\n
        Search the given value "value" on BST Object and return
        the BST Node with it\'s ".value" == value or return None if not found'''
        if self.value == value:
            return self
        left = self.left.find(value) if self.left is not None else None
        if left and left.value == value:
            return left
        right = self.right.find(value) if self.right is not None else None
        if right and right.value == value:
            return right

        return None

    def add(self, value):
        '''add(value) -> update BST if is a new value\n
        Add a new BST Node with given "value" as a leaf BST Node
        on it\'s right place depending on the passed "value" and
        current BST organization'''
        if self.find(value):
            print('value %s already in BST' % (value))

        elif self.value is None:
            self.value = value

        elif value < self.value:
            if self.left:
                self.left.add(value)
            else:
                self.left = BST(value)

        else:
            if self.right:
                self.right.add(value)
            else:
                self.right = BST(value)

        return self

def kthSmallestInBST(bst, k):
    '''kthSmallestInBST(BST, k) -> kth smallest  BST value | K <= count of BST nodes\n
    Return the kth smallest value from a inorder BST representation list'''
    def expand(bst):
        '''expand(BST) -> list\n
        Return a list of expanded BST nodes values on increasing order'''
        return expand(bst.left) + [bst.value] + expand(bst.right) if bst else []

    return expand(bst)[k - 1]

TREE = BST()
for i in [20, 22, 37, 10, 5, 12, 9, 52, 28]:
    TREE.add(i)
print(TREE.tostring())

print(kthSmallestInBST(TREE, 6))
