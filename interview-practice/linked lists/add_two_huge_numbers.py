'''Codefights interview practice - Linked List - addTwoHugeNumbers"'''
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

def format_zeros(number):
    '''format_zeros(int) -> str\n
    return a formated 4 digit number with leading zeros if needed as a string'''
    if number > 999:
        return str(number)
    elif number > 99:
        return "0" + str(number)
    elif number > 9:
        return "00" + str(number)
    else:
        return "000" + str(number)
    # return str(n) if n > 999 else "0" + str(n) if n > 99 else "00" + str(n) if n > 9 else "000" + str(n)

def list_reduce(linked_list):
    '''list_reduce(LinkedList) -> str\n
    Return a string representing the value of reduced Linked List with leading zeros if needed'''
    node, _str = linked_list, ""
    while node:
        _str += format_zeros(node.value)
        node = node.next
    return _str


def addTwoHugeNumbers(linked_listA, linked_listB):
    '''addTwoHugeNumbers(LinkedList, LinkedList) -> list\n
    Given 2 huge integers represented by linked lists. Each linked list
    element is a number from 0 to 9999 that represents a number with exactly 4 digits.
    The represented number might have leading zeros. Add up these huge
    integers and return the result in the same format.'''
    number = int(list_reduce(linked_listA)) + int(list_reduce(linked_listB))
    result = []
    while number // 10000 >= 1:
        result = [number % 10000] + result
        number = number // 10000
    result = [number % 10000] + result

    return result

LLA = LinkedList()
for v in [9876, 5432, 1999]:
    LLA.add(v)
print(LLA.tostring())

LLB = LinkedList()
for v in [1, 8001]:
    LLB.add(v)
print(LLB.tostring())

print(addTwoHugeNumbers(LLA, LLB))
