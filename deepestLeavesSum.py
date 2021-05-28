# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        roots = {}
        self.findSum(root,0,roots)
        return sum(roots[max(roots)])
        
    def findSum(self, root: TreeNode, level: int, roots: list):
        if root:
            self.findSum(root.left,level+1, roots)
            self.findSum(root.right,level+1, roots)
            roots.setdefault(level,[]).append(root.val)
