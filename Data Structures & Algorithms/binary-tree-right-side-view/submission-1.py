# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        q = collections.deque([root])

        while q:
            right = None
            length = len(q)
            for i in range(length):
                node = q.popleft()
                if node:
                    q.append(node.left)
                    q.append(node.right)
                    right = node
            if right:
                ans.append(right.val)

        return ans
        