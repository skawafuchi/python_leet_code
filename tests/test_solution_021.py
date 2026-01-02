from exercise_021.solution import Solution
from exercise_021.listnode import ListNode


class TestSolution():
    """
    Tests the solution for exercise 21. All values for input and output
    were provided by LeetCode.com
    """
    solution = Solution()

    def list_comparison(self, list_one: list, list_two: list,
                        solution_list: list) -> None:
        """
        Helper method to compare the solution with the assumed solution
        provided by LeetCode.

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
        merged_list = self.solution.mergeTwoLists(l1, l2)
        for num in solution_list:
            assert num == merged_list.val
            merged_list = merged_list.next

    def test_example_1(self):
        self.list_comparison([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4])

    def test_example_2(self):
        self.list_comparison([], [], [])

    def test_example_3(self):
        self.list_comparison([], [0], [0])
