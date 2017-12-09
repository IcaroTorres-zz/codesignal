'''Codefights interview practice - Linked List - mergeTwoLinkedLists"'''
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

def mergeTwoLinkedLists(linked_list1, linked_list2):
    '''Given two singly linked lists sorted in non-decreasing order,
    your task is to merge them. In other words, return a singly linked list,
    also sorted in non-decreasing order, that contains the elements from
    both original lists.'''
    curr = result = LinkedList(None)
    while linked_list1 and linked_list2:
        if linked_list1.value <= linked_list2.value:
            curr.next = linked_list1
            linked_list1 = linked_list1.next
        else:
            curr.next = linked_list2
            linked_list2 = linked_list2.next
        curr = curr.next
    curr.next = linked_list1 or linked_list2
    return result.next

LLA = LinkedList()
for v in [1, 2, 3]:
    LLA.add(v)
print(LLA.tostring())

LLB = LinkedList()
for v in [4, 5, 6]:
    LLB.add(v)
print(LLB.tostring())

print(mergeTwoLinkedLists(LLA, LLB).tostring()) # 1->2->3->4->5->6->None

LLA = LinkedList()
for v in [1, 1, 2, 4]:
    LLA.add(v)
print(LLA.tostring())

LLB = LinkedList()
for v in [0, 3, 5]:
    LLB.add(v)
print(LLB.tostring())

print(mergeTwoLinkedLists(LLA, LLB).tostring()) # 0->1->1->2->3->4->5->None


