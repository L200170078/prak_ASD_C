class Node(object):
	"""docstring for Node"""
	def __init__(self, data):
		self.data=data
		self.left=None
		self.right=None

class Tree(object):
	"""docstring for Tree"""
	def __init__(self):
		self.root=None

	def addData(self, node, newData):
		if self.root is None:
			self.root=Node(newData)
		else:
			if newData < node.data:
				# Akan ke kiri
				if node.left is None:
					node.left = Node(newData)
				else:
					self.addData(node.left, newData)
			else:
				# Akan ke Kanan
				if node.right is None:
					node.right=Node(newData)
				else:
					self.addData(node.right, newData)

	def tampilkanData(self, node, level=-1):
		level+=1
		if node is not None:
			self.tampilkanData(node.left, level)
			print(node.data, "Level ke", level)
			self.tampilkanData(node.right, level)

	def tinggiPohon(self, node):
		if node is None:
			return 0
		else:
			return max(self.tinggiPohon(node.left), self.tinggiPohon(node.right))+1

	def ukuran(self, node):
		if not node:
			return 0
		else:
			return 1 + (self.ukuran(node.left) + self.ukuran(node.right))


tree=Tree()
tree.addData(tree.root, 20)
tree.addData(tree.root, 10)
tree.addData(tree.root, 30)
tree.addData(tree.root, 9)
tree.addData(tree.root, 11)
tree.addData(tree.root, 21)
tree.addData(tree.root, 24)
tree.addData(tree.root, 35)

print("Ukuran Pohon Biner :", tree.ukuran(tree.root))
print("Tinggi Pohon Biner :", tree.tinggiPohon(tree.root))
print("Data Tiap Simpul + Level :")
tree.tampilkanData(tree.root)
# print(tree.root.right.right.right)
