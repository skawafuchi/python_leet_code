from solution import Solution
from listnode import ListNode

class TestSolution():
    solution = Solution()

    def list_comparison(self,list_one:list,list_two:list,solution_list:list)->None:
        l1 = ListNode().from_list(list_one)
        l2 = ListNode().from_list(list_two)
        merged_list = self.solution.mergeTwoLists(l1,l2)        
        for num in solution_list:
            assert num == merged_list.val
            merged_list = merged_list.next

    def test_example_1(self):
        self.list_comparison([1,2,4],[1,3,4],[1,1,2,3,4,4])
    
    def test_example_2(self):
        self.list_comparison([],[],[])
    
    def test_example_3(self):
        self.list_comparison([],[0],[0])