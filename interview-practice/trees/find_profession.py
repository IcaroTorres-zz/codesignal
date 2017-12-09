'''Consider a special family of Engineers and Doctors.
    This family has the following rules:

Everybody has two children.
The first child of an Engineer is an Engineer and the second child is a Doctor.
The first child of a Doctor is a Doctor and the second child is an Engineer.
All generations of Doctors and Engineers start with an Engineer.
We can represent the situation using this diagram:

                E
           /         \
          E           D
        /   \        /  \
       E     D      D    E
      / \   / \    / \   / \
     E   D D   E  D   E E   D
'''

# class code to test for hardcoding to display cases of few levels and pos
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

    def add_levels(self, levels):
        '''add_levels(int) -> Tree increased with int levels\n
        Return the Tree updated with given quantity of levels increased'''
        if levels == 0:
            return self
        if self.left is None and self.right is None:
            self.left = Tree("E") if self.value == "E" else Tree("D")
            self.right = Tree("D") if self.value == "E" else Tree("E")
            self.left = self.left.add_levels(levels - 1)
            self.right = self.right.add_levels(levels - 1)
        else:
            self.left = self.left.add_levels(levels)
            self.right = self.right.add_levels(levels)

        return self

def findProfession(level, pos):
    '''findProfession(int, int) -> str\n
    Return a string "Engineer" | "Doctor" depending on what profession value
    woul'd be contained on the Tree at especified level and position'''
    base = 'ed'
    for i in range(level - 2):
        base += base[len(base) // 2:] + base[:len(base) // 2]
    return 'Engineer' if base[pos - 1] == 'e' else 'Doctor'

TREE = Tree('E')
TREE.add_levels(6)
print(TREE.tostring())


print(TREE.tostring())
print(findProfession(25, 25163))
