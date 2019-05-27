# NOMOR 4 & NOMOR 5
class queue(object):
	"""docstring for queue"""
	def __init__(self):
		self.qlist=[]

	def isEmpty(self):
		return len(self.qlist)==0

	def __len__(self):
		return len(self.qlist)

	def enqueue(self, data):
		self.qlist.append(data)

	def dequeue(self):
		assert not self.isEmpty(), "Antrian Sedang KOSONG"
		return self.qlist.pop(0)

	def getFrontMost(self):
		return self.qlist[0]

	def getRearMost(self):
		return self.qlist[-1]

class PriorityQueue(object):
	"""docstring for PriorityQueue"""		
	def __init__(self):
		self.qlist=[]

	def __len__(self):
		return len(self.qlist)
		
	def isEmpty(self):
		return len(self.qlist)==0

	def enqueue(self, item, priority):
		entry=_PriorityQEntry(item,priority)
		self.qlist.append(entry)

	def dequeue(self):
		assert not self.isEmpty(), "Antrian Sedang KOSONG"
		index=0
		for i in range(1, len(self.qlist)):
			if self.qlist[i].priority < self.qlist[0].priority:
				index=i

		print(self.qlist[index].item)
		return self.qlist.pop(index)

class _PriorityQEntry(object):
	"""docstring for _PriorityQEntry"""
	def __init__(self, data, priority):
		self.item=data
		self.priority=priority

print("CLASS QUEUE")
s=queue()
s.enqueue(7)
s.enqueue(5)
s.enqueue(8)
print(s.qlist)
print("FRONT :", s.getFrontMost())
print("END :", s.getRearMost())

print("\nCLASS PRIORITY QUEUE")
s=PriorityQueue()
s.enqueue("Jeruk", 1)
s.enqueue("Tomat", 2)
s.enqueue("Mangga", 0)
s.dequeue()
s.dequeue()
s.dequeue()
# print(s.qlist[1].item)