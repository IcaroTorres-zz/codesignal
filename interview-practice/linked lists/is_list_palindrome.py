'''Codefights interview practice - Linked Lists - "isListPalindrome"'''
class LinkedList(object):
    '''LinkedList(value) -> Linked list Object {
    \t    self.value = value,
    \t    self.next = Linked list Object | None
    }
    A Linked list Object representing a Node with a ".value" porperty
    and ".next" pointing to "None" as default'''

    def __init__(self, value=None):
        '''".value" = a value to be stored and compared on new insertion or removal'''
        self.value = value
        self.next = None

    def add(self, value):
        '''add(value) -> appended LinkedList(value) after last Linked Node'''
        if self.value is None:
            self.value = value
        else:
            node = self
            while node.next is not None:
                node = node.next
            node.next = LinkedList(value)

    def tostring(self):
        '''simple function to display list nodes with values'''
        printable = str(self.value) + "->"
        node = self
        while node.next is not None:
            printable += str(node.next.value) + "->"
            node = node.next
        return printable + "None"


def isListPalindrome(linked_list):
    '''isListPalindrome(LinkedList) -> boolean\n
    Given a singly linked list of integers, determine whether or not it's a palindrome.'''
    _list = []
    node = linked_list
    while node is not None:
        _list.append(node.value)
        node = node.next

    return True if _list == _list[::-1] else False

LL = LinkedList()
for v in [0, 1, 0]:
    LL.add(v)
print(LL.tostring())
print(isListPalindrome(LL)) # True

K = 10
LL = LinkedList()
for v in [1, 2, 2, 3]:
    LL.add(v)
print(LL.tostring())
print(isListPalindrome(LL)) # False

K = 11
LL = LinkedList()
for v in [11, 0, 31, 13, 0, 13, 31, 0, 11]:
    LL.add(v)
print(LL.tostring())
print(isListPalindrome(LL))  # True
