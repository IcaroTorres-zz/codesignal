'''Tree script class to solve codefights interview practice Trees - "isTreeSymmetric"'''
class Tree(object):
    '''Tree(value) -> Simple Tree Object {
    \t    self.value = value,
    \t    self.left = Tree Object | None,
    \t    self.right = Tree Object | None
    }
    A Tree Object representing a Tree (or Sub-Tree)
    with a ".value" porperty and 2 Child BST Nodes
    ".left" and ".right" pointing to "None" as default'''

    def __init__(self, x):
        self.value = x
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

def isTreeSymmetric(tree):
    '''isTreeSymmetric(Tree) -> boolean\n
    Return if a Tree is symmetric, if left subtree is equal to reversed right subtree.
    In other words, sequence of subtree nodes on the same level (height) on left half of tree
    are equal to sequence of nodes on the same level on right half of tree.
    '''
    def expand_left(tree):
        '''expand_left(Tree) -> list\n
        Recursive expansion of left half tree nodes. Compose a list representation with all
        visited nodes replacing None with ['x']'''
        if tree is None:
            return ['x']
        else:
            return [tree.value] + expand_left(tree.left) + expand_left(tree.right)


    def expand_right(tree):
        '''expandLR(Tree) -> list\n
        Recursive expansion of right half tree nodes. Compose a list representation with all
        visited nodes replacing None with ['x']'''
        if tree is None:
            return ['x']
        else:
            return [tree.value] + expand_right(tree.right) + expand_right(tree.left)

    if tree is None:
        return True
    else:
        return expand_left(tree.left) == expand_right(tree.right)

TREE = Tree(10)
TREE.left, TREE.right = Tree(5), Tree(5)
TREE.left.left, TREE.left.right = Tree(3), Tree(6)
TREE.right.left, TREE.right.right = Tree(6), Tree(3)

print(isTreeSymmetric(TREE)) # True

TREE = Tree(10)
print(isTreeSymmetric(TREE)) # True

TREE = Tree(20)
TREE.left, TREE.right = Tree(5), Tree(5)
TREE.left.left, TREE.left.right = Tree(3), Tree(3)
TREE.right.left, TREE.right.right = Tree(4), Tree(4)
print(isTreeSymmetric(TREE)) # False

TREE = Tree(20)
TREE.left, TREE.right = Tree(10), Tree(10)
TREE.left.left, TREE.left.right = Tree(6), Tree(3)
TREE.right.left, TREE.right.right = Tree(6), Tree(3)
print(isTreeSymmetric(TREE))  # False
