from typing import Optional
from exercise_002.listnode import ListNode

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:  
        pointer_one = l1
        pointer_two = l2
        num_one_str = ""
        num_two_str = ""
        while (pointer_one != None or pointer_two != None):
            if (pointer_one != None):
                num_one_str = str(pointer_one.val) + num_one_str
                pointer_one = pointer_one.next
            if (pointer_two != None):
                num_two_str = str(pointer_two.val) + num_two_str
                pointer_two = pointer_two.next
        sum = int(num_one_str) + int(num_two_str)
        sum = str(sum)[::-1]
        return_list = None
        return_list_pointer = None
        for letter in sum:
            if (return_list == None):
                return_list = ListNode(int(letter))
                return_list_pointer = return_list
            else:
                return_list_pointer.next = ListNode(int(letter))
                return_list_pointer = return_list_pointer.next
        return return_list

            
            
            