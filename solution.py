#########################
# !!! SOLUTION CODE !!! #
#########################


class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root
   
    def getHeight(self,root):
        # CODE HERE
        
        left_node = 0
        right_node = 0

        if root.left is not None:
          left_node = 1 + self.getHeight(root.left)

        if root.right is not None:
          right_node = 1 + self.getHeight(root.right)

        return max(left_node, right_node)

        
T=int(input())
