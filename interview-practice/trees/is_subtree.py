'''Binary Search Tree script class to solve codefights interview practice Trees - "isSubtree"'''


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

def equals(bst1, bst2):
    '''equals(BST1,BST2) -> True | False\n
    Return True or False if BST Object 1 === BST Object 2,
    spreading this process to all children subtrees.'''
    if bst1 is None and bst2 is None:
        return True
    if bst1 is None or bst2 is None:
        return False

    left_eq = equals(bst1.left, bst2.left)
    right_eq = equals(bst1.right, bst2.right)
    return True if bst1.value == bst2.value and left_eq and right_eq else False


def isSubtree(bst1, bst2):
    '''isSubtree(BST1,BST2) -> True | False\n
    Returns if in bst1 there is an occurrence of some bst2 Object
    in which from it all subsequent children of both objects are equal,
    thus resulting in bst2 being subtree of bst1. '''

    if bst2 is None:
        return True
    if bst1 is None:
        return False
    if equals(bst1, bst2):
        return True
    return isSubtree(bst1.left, bst2) or isSubtree(bst1.right, bst2)

# dummy tests
TREE1 = BST()
TREE2 = BST()
TREE3 = BST()
for i in [15, 4, 3, 2, 7, 19, 16, 20]:
    TREE1.add(i)
print(TREE1.tostring())
for i in [4, 3, 2, 7]:
    TREE2.add(i)
print(TREE2.tostring())
print(isSubtree(TREE1, TREE2))
print(isSubtree(TREE1, TREE3))
for i in [19, 16, 20]:
    TREE3.add(i)
print(TREE3.tostring())
print(isSubtree(TREE1, TREE3))
