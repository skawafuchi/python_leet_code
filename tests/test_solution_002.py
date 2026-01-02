from exercise_002.solution import Solution
from exercise_002.listnode import ListNode


class TestSolution():
    """
    Tests the solution for exercise 2. All values for input and output
    were provided by LeetCode.com
    """
    solution = Solution()

    def list_comparison(self, list_one: list, list_two: list,
                        solution_list: list) -> None:
        """
        Helper method to compare the solution with the assumed 
        solution provided by LeetCode.

        Arguments:
            list_one (list): First list that will be converted
            into a linked list.
            list_two (list): Second list that will be converted
            into a linked list.
            solution_list (list): List that will be used to compare 
            the created solution against the LeetCode provided solution.
        """
        l1 = ListNode().from_list(list_one)
        l2 = ListNode().from_list(list_two)
        merged_list = self.solution.addTwoNumbers(l1, l2)        
        for num in solution_list:
            assert num == merged_list.val
            merged_list = merged_list.next

    def test_example_1(self):
        self.list_comparison([2, 4, 3], [5, 6, 4], [7, 0, 8])

    def test_example_2(self):
        self.list_comparison([0], [0], [0])

    def test_example_3(self):
        self.list_comparison([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9],
                             [8, 9, 9, 9, 0, 0, 0, 1])
