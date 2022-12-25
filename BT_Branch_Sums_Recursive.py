class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def branchSums(root):
    sumArray = []
    calculateBranchSums(root, 0, sumArray)
    return sumArray


def calculateBranchSums(node, runningSum, sumArray):
    if node is None:
        return
    newrunningSum = runningSum + node.value
    if node.left is None and node.right is None:
        sumArray.append(newrunningSum)
        return
        
    calculateBranchSums(node.left, newrunningSum, sumArray)
    calculateBranchSums(node.right, newrunningSum, sumArray)
    
