"""
File: add2.py
Name: Jack Chen
------------------------
"""

import sys


class ListNode:
    def __init__(self, data=0, pointer=None):
        self.val = data
        self.next = pointer


def add_2_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    #######################
    cur1 = l1
    cur2 = l2
    cur3 = None
    add_lst = []
    l3 = None
    add_digit = False  # Make sure if there is need to carry to the next digit.
    while cur1 is not None or cur2 is not None:  # While loop should stop when both cur1 and cur2 is None.
        if cur1 is None:
            a = 0
            b = cur2.val
        elif cur2 is None:
            a = cur1.val
            b = 0
        else:
            a = cur1.val
            b = cur2.val
        add_lst.append(a + b)
        if cur1 is None:  # Make sure the bug that None can not be add up will not appear.
            cur2 = cur2.next
        elif cur2 is None:
            cur1 = cur1.next
        else:
            cur1 = cur1.next
            cur2 = cur2.next
    for i in range(len(add_lst)):
        if add_lst[i] >= 10:  # All single val should be between 0-9.
            if i == len(add_lst)-1:  # If the last digit will carry to the next.
                add_digit = True
                add_lst.append(0)  # carry to the next digit
            add_lst[i] -= 10
            add_lst[i+1] += 1
        if l3 is None:  # Make sure to append the first digit
            l3 = ListNode(add_lst[0], None)
            cur3 = l3
        else:
            cur3.next = ListNode(add_lst[i], None)
            cur3 = cur3.next
            if i == len(add_lst)-2 and add_digit is True:  # make sure if l3 should carry to the next digit.
                cur3.next = ListNode(add_lst[-1], None)
    #######################
    return l3


def get_length(l1, l2):
    if len(l1) > len(l2):
        return len(l1)
    else:
        return len(l2)


####### DO NOT EDIT CODE BELOW THIS LINE ########


def traversal(head):
    """
    :param head: ListNode, the first node to a linked list
    -------------------------------------------
    This function prints out the linked list starting with head
    """
    cur = head
    while cur.next is not None:
        print(cur.val, end='->')
        cur = cur.next
    print(cur.val)


def main():
    args = sys.argv[1:]
    if not args:
        print('Error: Please type"python3 add2.py test1"')
    else:
        if args[0] == 'test1':
            l1 = ListNode(2, None)
            l1.next = ListNode(4, None)
            l1.next.next = ListNode(3, None)
            l2 = ListNode(5, None)
            l2.next = ListNode(6, None)
            l2.next.next = ListNode(4, None)
            ans = add_2_numbers(l1, l2)
            print('---------test1---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test2':
            l1 = ListNode(9, None)
            l1.next = ListNode(9, None)
            l1.next.next = ListNode(9, None)
            l1.next.next.next = ListNode(9, None)
            l1.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next.next = ListNode(9, None)
            l2 = ListNode(9, None)
            l2.next = ListNode(9, None)
            l2.next.next = ListNode(9, None)
            l2.next.next.next = ListNode(9, None)
            ans = add_2_numbers(l1, l2)
            print('---------test2---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test3':
            l1 = ListNode(0, None)
            l2 = ListNode(0, None)
            ans = add_2_numbers(l1, l2)
            print('---------test3---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        else:
            print('Error: Please type"python3 add2.py test1"')


if __name__ == '__main__':
    main()
