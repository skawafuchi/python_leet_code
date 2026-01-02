from exercise_021.listnode import ListNode
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        pointer_one = list1
        pointer_two = list2
        return_list = None
        return_list_pointer = None
        while(True):
            if (pointer_one is not None and pointer_two is None) or ((pointer_one is not None and pointer_two is not None) and pointer_one.val <= pointer_two.val):
                if not return_list:
                    return_list = ListNode(pointer_one.val)
                    return_list_pointer = return_list
                else:
                    return_list_pointer.next = ListNode(pointer_one.val)
                    return_list_pointer = return_list_pointer.next
                pointer_one = pointer_one.next
                continue
            if (pointer_two is not None and pointer_one is None) or ((pointer_one is not None and pointer_two is not None) and pointer_two.val <= pointer_one.val):
                if not return_list:
                    return_list = ListNode(pointer_two.val)
                    return_list_pointer = return_list
                else:
                    return_list_pointer.next = ListNode(pointer_two.val)
                    return_list_pointer = return_list_pointer.next
                pointer_two = pointer_two.next
                continue
            break
        return return_list