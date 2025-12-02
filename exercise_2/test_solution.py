from solution import Solution
from listnode import ListNode

class TestSolution():
    """
    Tests the solution for exercise 2. All values for input and output
    were provided by LeetCode.com
    """
    solution = Solution()
    def test_example_one(self):
        l1 = ListNode().from_list([2,4,3])
        l2 = ListNode().from_list([5,6,4])
        sum_list = self.solution.addTwoNumbers(l1,l2)
        assumed_answer = [7,0,8]
        for num in assumed_answer:
            assert num == sum_list.val
            sum_list = sum_list.next

    def test_example_two(self):
        l1 = ListNode().from_list([0])
        l2 = ListNode().from_list([0])
        sum_list = self.solution.addTwoNumbers(l1,l2)
        assumed_answer = [0]
        for num in assumed_answer:
            assert num == sum_list.val
            sum_list = sum_list.next

    def test_example_three(self):
        l1 = ListNode().from_list([9,9,9,9,9,9,9])
        l2 = ListNode().from_list([9,9,9,9])
        sum_list = self.solution.addTwoNumbers(l1,l2)
        assumed_answer = [8,9,9,9,0,0,0,1]
        for num in assumed_answer:
            assert num == sum_list.val
            sum_list = sum_list.next
        