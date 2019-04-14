# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        
        def calc(ancestors, elem):
            return max([abs(elem - ancestor) for ancestor in ancestors])
        
        def traverse(node, ancestors):
            if not node:
                return
            
            self.res = max(calc(ancestors, node.val), self.res)
            
            traverse(node.left, ancestors + [node.val])
            traverse(node.right, ancestors + [node.val])
                
        self.res = 0
        if not root:
            return 0
        traverse(root, [root.val])
        return self.res
