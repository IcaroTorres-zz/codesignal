'''Codefights interview practice - Linked List - reverseNodesInKGroups"'''
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

def reverse(start_node, end_node):
    '''reverse(LinkedList, LinkedList) -> [LinkedList, LinkedList]
    Given 2 linked list nodes (start_node and end_node), reverse the LinkedList nodes "pointers"
    starting from start_node till end_node to return a list of two Linked List object elements
    [updated start_node, end_node].'''
    head = LinkedList(None)
    head.next = start_node
    while head.next != end_node:
        aux = start_node.next
        start_node.next = aux.next
        aux.next = head.next
        head.next = aux
    return [start_node, end_node]


def reverseNodesInKGroups(linked_list, _k):
    '''reverseNodesInKGroups(LinkedList, +int) -> LinkedList\n
    Given a linked list, reverse its nodes k at a time and return the modified list.
    k is a positive integer that is less than or equal to the length of linked list.
    If the number of nodes in the linked list is not a multiple of k, then the nodes
    that are left out at the end should remain as-is.'''
    if not linked_list:
        return None
    head = LinkedList(None)
    head.next = linked_list
    start = head
    while start.next:
        end = start
        for i in range(_k - 1):
            end = end.next
            if not end.next:
                return head.next
        res = reverse(start.next, end.next)
        start.next = res[1]
        start = res[0]
    return head.next

LL = LinkedList()
for v in [1, 2, 3, 4, 5]:
    LL.add(v)
K = 2
print(LL.tostring())
print(reverseNodesInKGroups(LL, K).tostring()) # 2->1->4->3->5->None

LL = LinkedList()
for v in [1, 2, 3, 4, 5]:
    LL.add(v)
K = 1
print(LL.tostring())
print(reverseNodesInKGroups(LL, K).tostring()) # 1->2->3->4->5->None

LL = LinkedList()
for v in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]:
    LL.add(v)
K = 3
print(LL.tostring())
print(reverseNodesInKGroups(LL, K).tostring()) # 3->2->1->6->5->4->9->8->7->10->11->

