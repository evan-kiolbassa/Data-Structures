class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self
	
    def depthFirstSearch(self, array):
        '''
        Traversal of the graph structure
        using a depth first-search method.
    
            A
          / | \
          B C  D
         / \  / \
        E   F G  H
           / \  \
          I   J  K
        
        Final Output:
        [A, B, E, F, I, J, C, D, G, K, H]

        Begin Pseudo-Code Logic...

        array = []
        rootNode = A = name

        array.append(name)
        array = [A]

        Obtain child nodes of A
        nameChildrenNodes = [B, C, D]
        array.append(B)

        array = [A, B]

        Obtain child nodes of B
        childrenNodes = [E, F]
        array.append(E)
        
        array = [A, B, E]

        Child node of E is None

        Obtain child node of F
        childNodes = [I, J]

        array.append(I)
        no child node
        array.append(J)
        no child node

        array = [A, B, E, I, J]

        array.append(C)
        Children of C is None

        array = [A, B, E, I, J, C]
        
        array.append(D)

        array = [A, B, E, I, J, C, D]

        Obtain child nodes D
        childNodes = [G, H]

        array.append(G)

        array = [A, B, E, I, J, C, D, G]

        Obtain child nodes of G
        childNodes = [K]

        array.append(K)

        array = [A, B, E, I, J, C, D, G, K]

        children of K is None

        array.append(H)
        
        array = [A, B, E, F, I, J, C, D, G, K, H]

        traversal complete
        '''
        array.append(self.name)
		for child in self.children:
			child.depthFirstSearch(array)
		return array
	
