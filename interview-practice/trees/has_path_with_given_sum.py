'''Tree script class to solve codefights interview practice Trees - "hasPathWithGivenSum"'''
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

    def add(self, value):
        '''add(value) -> update Tree if is a new value\n
        Add a new Tree Node with given "value" as a leaf Tree Node
        on it\'s right place depending on the passed "value" and
        current Tree organization'''
        if self.value is None:
            self.value = value

        elif value < self.value:
            if self.left:
                self.left.add(value)
            else:
                self.left = Tree(value)

        else:
            if self.right:
                self.right.add(value)
            else:
                self.right = Tree(value)

        return self

def expand(tree, current, value):
    '''expand(Tree, int, int) -> True | False\n
    Return if expanding Tree Nodes from Tree root till reach Tree leafs there is a path which
    sum of Node.values resulting on given value. Visits all possible non None Tree Nodes
    by recurssion and keep current sum value of each path.'''
    current += tree.value
    if not tree.left and not tree.right:
        return True if current == value else False
    elif tree.left is not None and tree.right is not None:
        return expand(tree.left, current, value) or expand(tree.right, current, value)
    elif tree.left is not None and tree.right is None:
        return expand(tree.left, current, value)
    else:
        return expand(tree.right, current, value)

def hasPathWithGivenSum(tree, value):
    '''hasPathWithGivenSum(Tree, int) -> True | False\n
    Return True | False depending on the state and values inside the given Tree and the occurrence
    of a Node path expansion resulting on a sum == passed value'''
    if tree is not None:
        return expand(tree, 0, value)
    elif value == 0 and tree is None:
        return True
    else:
        return False
    
TREE = Tree(40)
for i in [25, 30, 21, 12, 0, 52, 6, 3, 9, 11, 27, 45]:
    TREE.add(i)
print(TREE.tostring())
print(hasPathWithGivenSum(TREE, 137)) #40 -> TREE.right 52 -> TREE.left 45
print(hasPathWithGivenSum(TREE, 20))  # 40 -> root.value > 20
print(hasPathWithGivenSum(TREE, 122))  # 40 -> TREE.left 25 -> TREE.right 30 -> TREE.light 27
