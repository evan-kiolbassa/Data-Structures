class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class TreeInfo:
    def __init__(self, diameter, height):
        self.diameter = diameter 
        self.height = height

def getTreeInfo(tree):
    if tree is None:
        return TreeInfo(0, 0)
        
    leftTreeInfo = getTreeInfo(tree.left)
    rightTreeInfo = getTreeInfo(tree.right)

    largestHeightThroughRoot = leftTreeInfo.height + rightTreeInfo.height
    currentMaxDiameter = max(leftTreeInfo.diameter, rightTreeInfo.diameter)
    currentDiameter = max(largestHeightThroughRoot, currentMaxDiameter)
    currentHeight = 1 + max(leftTreeInfo.height, rightTreeInfo.height)

    return TreeInfo(currentDiameter, currentHeight)
        
def binaryTreeDiameter(tree):
    '''
                1
               / \
              3   2
             / \
            7   4
           /     \
          8       5
         /         \
        9           6

    The diameter of a binary tree is the length
    of its longest path. The longest path does not need to 
    pass through the root.

    Final output:
    6 Edges
    9 -> 8 -> 7 -> 3 -> 4 -> 5 -> 6

    =============================
    Depth-First Search Tree Traversal -
    Traversing left side of tree until
    None-type node
    =============================
                1
               / \
              3   2
             / \
            7   4
           /     \
          8       5
         /         \
        9           6

    currentNode = None
        # (diameter, height)
        leftSubtree = (0, 0)
        rightSubtree = (0, 0)

    longestRootPath = leftSubTreeHeight(0) + rightSubTreeHeight(0) = 0
    maxSubTreeDiameter = max(leftSubTreeDiam(0), rightSubTreeDiam)(0) = 0
    currentDiameter = max(maxSubTreeDiameter(0), longestRootPath(0)) = 0
    currentTreeHeight = 1 + max(leftSubTreeHeight(0), rightSubTreeHeight(0)) = 1

    currentNode = 9
    longestRootPath = leftSubTreeHeight(1) + rightSubTreeHeight(0) = 1
    maxSubTreeDiameter = max(leftSubTreeDiam(0), rightSubTreeDiam)(0) = 0
    currentDiameter = max(maxSubTreeDiameter(0), longestRootPath(1)) = 1
    currentTreeHeight = 1 + max(leftSubTreeHeight(1), rightSubTreeHeight(0)) = 2

    currentNode = 8
    longestRootPath = leftSubTreeHeight(2) + rightSubTreeHeight(0) = 2
    maxSubTreeDiameter = max(leftSubTreeDiam(1), rightSubTreeDiam)(0) = 1
    currentDiameter = max(maxSubTreeDiameter(1), longestRootPath(2)) = 2
    currentTreeHeight = 1 + max(leftSubTreeHeight(2), rightSubTreeHeight(0)) = 3

    *******************************
    Skipping to Node 3
    *******************************
    currentNode = 3
    longestRootPath = leftSubTreeHeight(4) + rightSubTreeHeight(0) = 4
    maxSubTreeDiameter = max(leftSubTreeDiam(3), rightSubTreeDiam)(0) = 3
    currentDiameter = max(maxSubTreeDiameter(3), longestRootPath(4)) = 4
    currentTreeHeight = 1 + max(leftSubTreeHeight(4), rightSubTreeHeight(0)) = 5
    '''
    return getTreeInfo(tree).diameter
