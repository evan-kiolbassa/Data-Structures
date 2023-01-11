def nodeDepths(root):
    '''

                1
               /  \
              2      3   
             /  \   / \
            4    5 6  7
           /  \
          8    9

    Final Output = 16

    // The depth of the node with value 2 is 1
    // the depth of the node with value 3 is 1
    // the depth of the node with value 4 is 2
    // the depth of the node with value 5 is 2

    Begin Pseudo-Code Logic
    depthSum = 0
    stack = [{"node": root, "depth": 0}]
    
    while len(stack) > 0:
        
        *******************************************
        While-Loop Iteration Process
        *******************************************
        currentDict = stack.pop()
        currentNode = currentDict["node"] = 0
        if currentNode is None:
            continue
        stack = []
        
        depthSum += currentDict["depth"] = 0
    
        stack.append({"node": currentNode.left, "depth": 0 + 1})
        stack.append({"node": currentNode.right, "depth": 0 + 1})
    
        stack = [
        {"node": currentNode.left = 2, "depth": 0 + 1},
        {"node": currentNode.right = 3, "depth": 0 + 1}
        ]

        currentDict = stack.pop()

        stack = [
        {"node": currentNode.left = 2, "depth": 0 + 1},
        ]

        currentNode = currentDict["node"] = 3
        calculate depthSum
        depthSum += currentDict["depth"] = 0 + 1 = 1

        stack.append({"node": currentNode.left, "depth": 1 + 1})
        stack.append({"node": currentNode.right, "depth": 1 + 1})

        stack = [
        {"node": currentNode.left = 2, "depth": 1},
        {"node": currentNode.left = 6, "depth": 2},
        {"node": currentNode.right = 7, "depth": 2}
        ]

        #############################################
        Process repeats until stack length is zero
        #############################################

    End Pseudo-Code Logic
    '''

    
    depthSum = 0
    stack = [{"node": root, "depth": 0}]

    while len(stack) > 0:
        currentDict = stack.pop()
        currentNode = currentDict["node"]
        if currentNode is None:
            continue
        depthSum += currentDict["depth"]

        stack.append({"node": currentNode.left, "depth": currentDict["depth"] + 1})
        stack.append({"node": currentNode.right, "depth": currentDict["depth"] + 1})

    return depthSum



# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
