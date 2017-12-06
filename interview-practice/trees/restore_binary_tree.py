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

def restoreBinaryTree(bst_inorder_list, bst_preorder_list):
    '''Given 2 lists (inorder and preorder) representing BST
    "inorder traversal" and "preorder traversal", return a
    BST Object structured with all corresponding children"'''
    bst = BST(bst_preorder_list[0])
    left_inorder = bst_inorder_list[:bst_inorder_list.index(bst_preorder_list[0])]
    right_inorder = bst_inorder_list[bst_inorder_list.index(bst_preorder_list[0]) + 1:]
    left_preorder = bst_preorder_list[1: len(left_inorder) + 1]
    right_preorder = bst_preorder_list[len(left_inorder) + 1:]

    if left_inorder:
        bst.left = restoreBinaryTree(left_inorder, left_preorder)
    if right_inorder:
        bst.right = restoreBinaryTree(right_inorder, right_preorder)

    return bst


inorder = [2, 10, 15, 16, 17, 21, 22, 29, 30, 33, 38, 41]
preorder = [21, 15, 10, 2, 17, 16, 33, 29, 22, 30, 38, 41]
print(restoreBinaryTree(inorder, preorder).tostring())
help(BST)
