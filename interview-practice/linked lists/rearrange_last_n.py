'''Codefights interview practice - Linked List - rearrangeLastN"'''
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


def rearrangeLastN(linked_list, number):
    '''rearrangeLastN(LinkedList, int) -> LinkedList\n
    Given a singly linked list of integers l and a non-negative integer n,
    move the last n list nodes to the beginning of the linked list.'''
    if linked_list is None or number == 0:
        return linked_list

    last = head = linked_list
    while number > 0 and last is not None:
        last = last.next
        number -= 1

    if number >= 0 and not last:
        return linked_list

    while last.next:
        head = head.next
        last = last.next

    new_head = head.next
    head.next = None
    last.next = linked_list

    return new_head

LL = LinkedList()
for v in [1, 2, 3, 4, 5]:
    LL.add(v)
N = 3
print(LL.tostring())
print(rearrangeLastN(LL, N).tostring()) # 3->4->5->1->2->None

LL = LinkedList()
for v in [1, 2, 3, 4, 5, 6, 7]:
    LL.add(v)
N = 1
print(LL.tostring())
print(rearrangeLastN(LL, N).tostring()) # 7->1->2->3->4->5->6->None

LL = LinkedList()
for v in [3, 2, 1, 21, 32, 43, 54, 12, 23, 34, 45]:
    LL.add(v)
N = 7
print(LL.tostring())
print(rearrangeLastN(LL, N).tostring()) # 32->43->54->12->23->34->45->3->2->1->21->None
