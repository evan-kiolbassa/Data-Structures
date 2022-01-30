class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
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
        A method that allows for the insertion of an existing node, prior to a nnode specified in the argument. 
        This method is also used for setting the list head when the structure is non-empty.

        Performs an initial check if the node to be inserted is equivalent to both the head and tail (inserting a redundant node into a single value list, head = tail),
        and then returns the linkedlist object.

        The remove method is applied to the node to be moved.

        The nodeToInsert prev marker becomes the node previous to the node originally in that position, and the next marker becomes the node being replaced at that position.

        If the node argument prev pointer is null, the node becomes the head of the list. If the node is non-null, 
        the next marker for the prev node is updated with the nodeToInsert and the prev marker for the replaced node is updated to be the inserted node
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
        '''
        Method that removes nodes with specific values. 
        Traversal of the linked list starting from the head,
        while the node is not null. If the node key has a value
        equal to the input parameter, the remove method is used 
        to change the adjacent node pointers.
        '''
        node = self.head
		while node is not None:
			nodeToRemove = node
			node = node.next
			if nodeToRemove.value == value:
				self.remove(nodeToRemove)

    def remove(self, node):
        '''
        A method that removes a specific LinkedList node.
        If the node to be removed is the head, the head becomes the forward adjacent node.
        If it is the tail, the tail becomes the previous adjacent node.
        All other nodes use the removeNodeBindings method.
        '''
        if node == self.head:
			self.head = self.head.next
		if node == self.tail:
			self.tail = self.tail.prev
		self.removeNodeBindings(node)
		
    def containsNodeWithValue(self, value):
        '''
        Traversal of the LinkedList structure starting at the list head.
        Accesses the value of each node key and compares it to the desired 
        value. Returns the non-null value.
        '''
        node = self.head
		while node is not None and node.value != value:
			node = node.next
		return node is not None
	
	def removeNodeBindings(self, node):
		'''
		Initiates the removal of linked list node bindings for the remove method.
        First, checks if the previous node is not null, then updates the previous node's markers and 
        updating the next node markers as well. This effectively removes the desired node and maintains the
        structure of the linked list
		'''
		if node.prev is not None:
			node.prev.next = node.next
		if node.next is not None:
			node.next.prev = node.prev
		node.prev = None
		node.next = None