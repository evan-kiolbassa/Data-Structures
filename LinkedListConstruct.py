class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    '''
    <- 1 <-> 2 <-> 3 <-> 4 <-> 5 ->
    '''
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
		if self.head is None:
        	self.head = node
			self.tail = node
			return
		self.insertBefore(self.head, node)
	
    def setTail(self, node):
        if self.tail is None:
			self.setHead(node)
			return
		self.insertAfter(self.tail, node)

    def insertBefore(self, node, nodeToInsert):
        '''
        nodeToInsert = 5
        node = 3
                              Node      nodeToInsert  
                               |           | 
                <- 1 <-> 2 <-> 3 <-> 4 <-> 5 ->
                
                =============================
                Removing the five node
                =============================
                node.prev     node     node.next
                        \      |       /
                <- 1 <-> 2 <-> 3 <-> 4 ->
                                    /      \                   
                   nodeToInsert.prev        nodeToInsert.next

                =============================
                Redefining the nodeToInsert pointers
                to align with defined node to insert
                before.
                =============================

                     node.prev      node    node.next
                        \            |      /
                <- 1 <-> 2 <-> 5 <-> 3 <-> 4 ->
                         /            \                   
        nodeToInsert.prev             nodeToInsert.next
        '''
        if nodeToInsert == self.head and nodeToInsert == self.tail:
			return
		self.remove(nodeToInsert)
		nodeToInsert.prev = node.prev
		nodeToInsert.next = node
		if node.prev is None:
			self.head = nodeToInsert
		else:
			node.prev.next = nodeToInsert
		node.prev = nodeToInsert
			
    def insertAfter(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
			return
		self.remove(nodeToInsert)
		nodeToInsert.prev = node
		nodeToInsert.next = node.next
		if node.next is None:
			self.tail  = nodeToInsert
		else:
			node.next.prev = nodeToInsert
		node.next = nodeToInsert

    def insertAtPosition(self, position, nodeToInsert):
        if position == 1:
			self.setHead(nodeToInsert)
			return
		insertPosition = 1
		node = self.head
		while node is not None and insertPosition != position:
			node = node.next
			insertPosition += 1
		if node is not None:
			self.insertBefore(node,nodeToInsert)
		else:
			self.setTail(nodeToInsert)

    def removeNodesWithValue(self, value):
        node = self.head
		while node is not None:
			nodeToRemove = node
			node = node.next
			if nodeToRemove.value == value:
				self.remove(nodeToRemove)

    def remove(self, node):
        if node == self.head:
			self.head = self.head.next
		if node == self.tail:
			self.tail = self.tail.prev
		self.removeNodeBindings(node)
    
    def containsNodeWithValue(self, value):
        node = self.head
		while node is not None and node.value != value:
			node = node.next
		return node is not None
	
	def removeNodeBindings(self, node):
		'''
		Initiates the removal of linked list node bindings for the remove method.

                        Node.prev   Node    Node.next 
                              \      |      /
                      <- 1 <-> 2 <-> 3 <-> 4 <-> 5 ->
                                     |
                                Node.prev.next will point to 4
                                      &
                                Node.next.prev will point to 2

                                Node.prev = None
                                Node.next = None

                                All pointers of 3 node are removed returning...

                     <- 1 <-> 2 <-> 4 <-> 5 ->
		'''
		if node.prev is not None:
			node.prev.next = node.next
		if node.next is not None:
			node.next.prev = node.prev
		node.prev = None
		node.next = None
