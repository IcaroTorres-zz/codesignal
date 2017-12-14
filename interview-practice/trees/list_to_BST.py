'''Binary Search Tree script to solve codefights interview practice Trees - "restoreBinaryTree"'''


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

        if isinstance(value, list):
            aux = list_to_bst(value)
            self.value = aux.value
            self.left = aux.left
            self.right = aux.right
        else:
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

    def add(self, value):
        '''add(value) -> update BST if is a new value\n
        Add a new BST Node with given "value" as a leaf BST Node
        on it\'s right place depending on the passed "value" and
        current BST organization'''

        if self.value is None:
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

def list_to_bst(_list):
    '''list_to_bst(list) -> BST Object'''
    tmp = sorted(_list)
    tmp = tmp[len(tmp)//2]
    _list[_list.index(tmp)] = _list[0]
    _list[0] = tmp
    tree = BST()
    for element in _list:
        tree.add(element)
    return tree

SAMPLELIST = [21, 15, 10, 2, 17, 16, 33, 29, 22, 30, 38, 41]
print(BST(SAMPLELIST).tostring())
