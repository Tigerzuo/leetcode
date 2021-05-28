# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        nodes = [cloned]
        
        while nodes:
            for node in nodes:
                if node.val == target.val:
                    return node
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
