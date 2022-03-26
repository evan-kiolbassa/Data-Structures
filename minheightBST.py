def minHeightBst(array):
    return minHeightConstructor(array, None, 0, len(array) - 1)

def minHeightConstructor(array,bst, startidx, endidx):
	if startidx > endidx:
		return
	array.sort()
	nodeToInsert = (startidx + endidx) // 2
	valueToInsert = array[nodeToInsert]
	if bst is None:
		bst = BST(valueToInsert)
	else:
		bst.insert(valueToInsert)
	minHeightConstructor(array, bst, startidx, nodeToInsert - 1)
	minHeightConstructor(array, bst, nodeToInsert + 1, endidx)
	return bst
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
