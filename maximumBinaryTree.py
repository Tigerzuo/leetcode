# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:        
        def buildTree (inorder, start, end):
            if start > end:
                return None
            
            # If this is the only element in 
            # inorder[start..end], then return it 
            if start == end:
                return TreeNode(inorder[start])
            
            i = max(inorder[start:end+1])             
            index = inorder.index(i)

            # Pick the maximum value and make it root 
            root = TreeNode(i) 

            # Using index in Inorder traversal, 
            # construct left and right subtress 
            root.left = buildTree (inorder, start, index - 1) 
            root.right = buildTree (inorder, index + 1, end) 

            return root
        return buildTree(nums,0,len(nums)-1)
