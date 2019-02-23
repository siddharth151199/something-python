class Node():
	#Function to initialize node
	def __init__(self, val = None):
		self.val = val
		self.next = None
		
		
class ListNode(Node):
	#Function to initialize Linked List
	def __init__(self):
		self.head = None
	
	#Function to print the list
	def print_list(self):
		printval = self.head
		print("The list is: " + '\r')
		while printval is not None:
			print(printval.val)
			printval = printval.next
	
	#Function to insert at the begenning
	def insert_node_begenning(self, newval = None):
		newval = int(input("Enter data to be added at begenning: "))
		NewNode = Node(newval)
		NewNode.next = self.head
		self.head = NewNode
		
	#Function to insert at the end
	def insert_node_end(self, newval = None, ptr = None, preptr = None):
		newval = int(input("Enter data to be added at end: "))
		NewNode = Node(newval)
		NewNode.next =  None
		ptr = self.head
		while ptr is not None:
			preptr = ptr
			ptr = ptr.next
			
		preptr.next = NewNode
			
		
list = ListNode()
while True:
	print("1.Insertbegenning\n2.InsertEnd\n3.PrintList\n4.Exit")
	choice = int(input("Enter your choice as number: "))
	if choice == 1:
		list.insert_node_begenning()
	elif choice == 2:
		list.insert_node_end()
	elif choice == 3:
		list.print_list()
	elif choice == 4:
		exit(0)
	
		
	
		
		
