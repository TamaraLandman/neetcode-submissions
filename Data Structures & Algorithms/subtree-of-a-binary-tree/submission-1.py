# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: return True
        if not root: return False
        
        if self.dfs(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


    def dfs(self, node, sNode):
        if node is None and sNode is None:
            return True
        if node and sNode and node.val == sNode.val:
            return self.dfs(node.left, sNode.left) and self.dfs(node.right, sNode.right)

        return False
        
        