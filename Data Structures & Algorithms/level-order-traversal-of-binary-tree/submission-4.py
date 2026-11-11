# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # use BFS
        queue = deque([root])

        # need to make sure each level is traversed fully
        level_collection = []
        while queue:
            level_list = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    level_list.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if level_list:
                level_collection.append(level_list)
        
        return level_collection
