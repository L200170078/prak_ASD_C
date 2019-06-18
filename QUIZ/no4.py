class SimpulPohon(object):
	"""docstring for SimpulPohon"""
	def __init__(self, data):
		self.data=data
		self.kiri=None
		self.kanan=None
	
def inorder(node):
	if node is not None:
		inorder(node.kiri)
		print(node.data)
		inorder(node.kanan)
def postorderTraversal(node):
	if node is not None:
		postorderTraversal(node.kiri)
		postorderTraversal(node.kanan)
		print(node.data)
def tinggiPohon(node):
		if node is None:
			return 0
		else:
			return max(tinggiPohon(node.kiri), tinggiPohon(node.kanan))+1
		
x=SimpulPohon("X")
d=SimpulPohon("D")
y=SimpulPohon("Y")
n=SimpulPohon("N")
o=SimpulPohon("O")
s=SimpulPohon("S")
a=SimpulPohon("A")
v=SimpulPohon("V")
w=SimpulPohon("W")
q=SimpulPohon("Q")

x.kiri=d
x.kiri.kanan=n
x.kiri.kanan.kiri=s
x.kiri.kanan.kiri.kiri=w
x.kiri.kanan.kiri.kanan=q
x.kanan=y
x.kanan.kanan=o
x.kanan.kanan.kiri=a
x.kanan.kanan.kanan=v

print("Inorder Traversal")
inorder(x)
print("\n")
print("Postorder Traversal")
postorderTraversal(x)

# print("\n")
# print(tinggiPohon(x)-1)