class ListNode:
    def __init__(self, val=0, next=None):
        """
        Definition for singly-linked list. Provided by LeetCode.com
        """
        self.val = val
        self.next = next

    @classmethod
    def from_list(cls,linked_list_values:list[int]):
        """
        Helper method to create a linked list from a list of integers.

        Arguments:
            linked_list_values list[int]: A list of int values to be used as the links in the linked list.

        Returns:
            A ListNode with next values being subsequent values of the list.
        """
        return_list = None
        last_pointer = None
        for val in linked_list_values:
            if (not return_list):
                return_list = cls(val)
                last_pointer = return_list
            else:
                last_pointer.next = ListNode(val)
                last_pointer = last_pointer.next

        return return_list
    