# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        tree1_list = self.in_order(root1)
        tree2_list = self.in_order(root2)
        final_list = tree1_list + tree2_list
        final_list.sort()
        return final_list
        
    def in_order(self,root:TreeNode) -> List[int]:            
        ele_list = []
        if root:
            ele_list = ele_list + self.in_order(root.left)
            ele_list.append(root.val)
            ele_list = ele_list + self.in_order(root.right)
        return ele_list
        