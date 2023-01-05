class Node:
    
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        '''
        Traversal of the graph structure
        from left to right by level.
    
            A
          / | \
          B C  D
         / \  / \
        E   F G  H
           / \  \
          I   J  K

        Final Output:
        finalArray = [A, B, C, D, H, I, J, K]

        Pseudo-code Logic Begin...
        Initiate final array
        finalArray = []
        queue = []

        append root node to queue
        queue = [A] 
        currentNode = queue.head()
        queue.pop()

        Append currentNode to final array
        finalArray = [A]

        Add children nodes to queue
        queue = [B, C, D]
        currentNode = B
        queue.pop()
        queue = [C, D]
        finalArray = [A, B]
        queue = [C, D, E, F]
        ......
        iterate until no child nodes exist and queue is depleted
        '''

        queue = [self]
        
        while len(queue) > 0:
            currentNode = queue.pop(0)
            array.append(currentNode.name)
            for children in currentNode.children:
                queue.append(children)
        return array
