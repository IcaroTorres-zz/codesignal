'''Codefights interview practice - Linked Lists - "removeKFromList"'''
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

def removeKFromList(linked_list, value):
    '''removeKFromList(LinkedList, value) -> LinkedList\n
    Given a singly linked list of integers l and an integer k,
    remove all elements from list l that have a value equal to k.'''
    node = linked_list
    while node is not None:
        if node.next and node.next.value == value:
            node.next = node.next.next
        else:
            node = node.next

    return linked_list.next if linked_list and linked_list.value == value else linked_list

K = 3
LL = LinkedList()
for v in [3, 1, 2, 3, 4, 5]:
    LL.add(v)
print(LL.tostring())
print(removeKFromList(LL, K).tostring()) # 1->2->4->5->None

K = 10
LL = LinkedList()
for v in [1, 2, 3, 4, 5, 6, 7]:
    LL.add(v)
print(LL.tostring())
print(removeKFromList(LL, K).tostring()) # 1->2->3->4->5->6->7->None 10 not in LL

K = 11
LL = LinkedList()
for v in [11, 21, 32, 48, 52, 60, 79, 13, 11]:
    LL.add(v)
print(LL.tostring())
print(removeKFromList(LL, K).tostring()) # 21->32->48->52->60->79->13->None
