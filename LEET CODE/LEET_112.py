# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:  # 트리가 비어있다면 False 
            return False


        # 리프 노드에 도달했을 때, targetSum - root.val == 0 확인
        if not root.left and not root.right:
            if targetSum - root.val == 0:
                return True
            else:
                return False

        # 왼쪽 또는 오른쪽 서브트리에서 경로 합을 찾기 위해 재귀 호출
        targetSum -= root.val
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)


