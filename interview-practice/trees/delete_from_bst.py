'''Binary Search Tree script class to solve codefights interview practice Trees - "deleteFromBST"'''

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
        printable = '{"value":'+ str(self.value)
        if self.left:
            printable += ',\n' + spaces + '"left": ' + self.left.tostring(identation+1) + '}'
        else:
            printable += ',\n' + spaces + '"left": None'
        if self.right:
            printable += ',\n' + spaces + '"right": ' + self.right.tostring(identation+1) + '}'
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

    def flatten(self):
        '''flatten(BST) -> [list with inorder traversal BST values] | []\n
        Return a "BST inorder traversal" list Object. Ex: "[1,3,4,7,9,11...]"'''
        def flat(bst):
            '''Recursive "BST inorder traversal"'''
            if bst.value is None:
                return []
            left = flat(bst.left) if bst.left else []
            right = flat(bst.right) if bst.right else []
            return left + [bst.value] + right

        return flat(self)

    def inorder(self):
        '''inorder(BST) -> Print "BST inorder traversal" values as string'''
        def inn(bst):
            '''Internal recursive concat loop '''
            left = inn(bst.left) if bst.left else ""
            right = inn(bst.right) if bst.right else ""
            return str(left) + " " + str(bst.value) + " " + str(right)

        print(inn(self))

    def predecessor(self):
        '''predecessor(BST) -> value | all other BST children values < value < BST.value\n
        Get highest value (predecessor) of a BST'''
        while self.right is not None:
            self = self.right

        return self.value

    def remove_right(self):
        '''remove_right(BST) -> BST subtree to replace the one to be removed as follows:\n
        Replace BST by it's ".left" subtree if ".right" points to None,
        Can also be replaced by None no childs. When ".right" not points to None,
        applies this recursive function to it. Return passed BST changed in each
        recursive call'''
        if self.right is None:
            return self.left # can return None if not self.left
        else:
            self.right = self.right.remove_right()
        return self

    def process(self, value):
        '''process(value) -> updated BST reorganized with value removed as follows:\n
        Process the BST against searched value. Returning None if already an empty BST,
        replacing removed node by the highest value after it, Or recursively search on
        (".left" or ".right"), if searched value > or < then ".value"'''
        if value == self.value:
            if self.left:
                self.value, self.left = self.left.predecessor(), self.left.remove_right()
            else: self = self.right
        elif value < self.value:
            self.left = self.left.process(value) if self.left is not None else None
        elif value > self.value:
            self.right = self.right.process(value) if self.right is not None else None
        return self

    def deleteFromBST(self, query_list):
        '''deleteFromBST(BST) -> updated BST with a step-by-step removal process as follows:\n
        Delete each BST Node with values of a given "query list" List Object if that value is
        on BST. Also reorganize the BST structure if needed to maintain all BST structure rules'''

        for value in query_list:
            self = self.process(value)

        return self

INSERTS = [56, 36, 88, 102, 39, 28, 11, 24, 13, 8, 7, 20, 17, 45, 101, 102, 24, 13]
QUERIES = [88, 24, 11, 101, 21, 45, 51, 56]
ROOT = BST()

for i in INSERTS:
    ROOT.add(i)
INORDER_LIST = ROOT.flatten()
ROOT.inorder()
print(INORDER_LIST)
RESULT = ROOT.deleteFromBST(QUERIES)
if RESULT:
    print(RESULT.tostring())
else:
    print(None)

help(BST)
