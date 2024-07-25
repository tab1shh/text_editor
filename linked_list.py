class Node:
    def __init__(self, data):
        self.data = data # data is stored here
        self.next = None # points to next node

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data) # a new node is created with the provided data
        if not self.head: # if the linked list is empty
            self.head = new_node # the new node becomes the head of the list
            return
        last = self.head # starts from the head of the list to the find the last node
        while last.next: # loops through the list till it finds the last node
            last = last.next # moves to the next node in the list
        last.next = new_node # links the last node to the new node, making it so it's appending it to the end

    def delete_last(self): 
        # checks if linked list is empty
        # if head of linked list is none, the method returns none showing there is no element to delete
        if not self.head:
            return None
        # checks if there is only one element in linked list
        # if head node doesnt have a next node, method stores 'head' node in 'temp', sets 'head' to 'None' (emptying list) and returns data of the deleted node
        if not self.head.next: # if theres only one head, remove it and return its data
            temp = self.head 
            self.head = None 
            return temp.data # return data from removed head
        # travseres the linked list to find the second to last node
        # sets 'last' to 'head' and iterates through the list until 'last.next.next' os 'None', so 'last' points to second to last node
        last = self.head # start at first head
        while last.next.next: # move to head before the last 
            last = last.next
        # deletes last node and returns data
        # stores the last node in 'temp', sets 'last.next' to 'None', removing the last node from the list and returns the data of the deleted node
        temp = last.next
        last.next = None
        return temp.data
    
    def __str__(self):
        # initializes variables needed for converting the linked list to string
        # create an empty list 'out' to store data of each node. set 'current' to the 'head' of the linked list to start traversal
        out = []
        current = self.head
        # traverse linked list and collect data of each node
        # while 'current' is not 'None' ie there are still nodes to traverse, the method appends the data of 'current' to 'out' and moves to the next node by setting 'current' to 'current.next'
        while current:
            out.append(current.data)
            current = current.next
        # convert the collected data to a string
        return ''.join(out)