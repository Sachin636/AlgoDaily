# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


#######  APPROACH 1 ##########
##############################

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        node_in_b = set()

        while headB:
            node_in_b.add(headB)
            headB = headB.next

        while headA:
            if headA in node_in_b:
                return headA
            headA = headA.next

        return None

# Idea #
# traverse through the node using a pointer and
# store the nodes in a set
# while traversing using other node if you find the
# node in set return it as answer
# else retrun None
########

# RUNTIME #
# O( M + N )  where M and N are length of lists

# SPACE #
# O(N) # space used for the hash map

##### End Approach 1 ##########
###############################


#######  APPROACH 2 ##########
##############################
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        pass

##### End Approach 2 ##########
###############################
