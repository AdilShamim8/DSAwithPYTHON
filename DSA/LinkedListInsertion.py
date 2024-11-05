'''
ALGORITHM InsertAtPosition
1. Start.
2. Create a new node.
3. Set newNode.data to the new value.
4. If position is 0:
    a. Set newNode.next to head.  // Link new node to current head
    b. Set head to newNode.  // Update head to new node
5. Else:
    a. Set current to head.
    b. For i from 0 to position - 1:
        i. If current is null, print "Position out of bounds." and exit.
        ii. Set previous to current.  // Keep track of the previous node
        iii. Set current to current.next.
    c. Set newNode.next to current.  // Link new node to current
    d. Set previous.next to newNode.  // Link previous node to new node
6. End.
'''



class Node:
    def __init__(self, data):
        self.data = data  # Store data
        self.next = None  # Pointer to the next node

class SinglyLinkedList:
    def __init__(self):
        self.head = None  # Initialize head to None

    # Insertion at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)  # Create a new node
        new_node.next = self.head  # Link new node to current head
        self.head = new_node  # Update head to new node

    # Insertion at the end
    def insert_at_end(self, data):
        new_node = Node(data)  # Create a new node
        if self.head is None:  # Check if the list is empty
            self.head = new_node  # The list was empty, so make this node the head
            return
        
        current = self.head
        while current.next is not None:  # Traverse to the last node
            current = current.next
        
        current.next = new_node  # Link the last node to the new node

    # Insertion at a specific position
    def insert_at_position(self, data, position):
        new_node = Node(data)  # Create a new node
        if position == 0:  # Insert at the beginning
            new_node.next = self.head  # Link new node to current head
            self.head = new_node  # Update head to new node
            return
        
        current = self.head
        for i in range(position - 1):  # Traverse to the specified position
            if current is None:
                print("Position out of bounds.")
                return
            current = current.next

        new_node.next = current.next  # Link new node to current
        current.next = new_node  # Link previous node to new node

    # Traversing the list
    def traverse(self):
        current = self.head
        while current is not None:
            print(current.data)  # Print data of the current node
            current = current.next

# Example usage:
linked_list = SinglyLinkedList()
linked_list.insert_at_end(10)  # List: 10
linked_list.insert_at_end(20)  # List: 10 -> 20
linked_list.insert_at_beginning(5)  # List: 5 -> 10 -> 20
linked_list.insert_at_position(15, 2)  # List: 5 -> 10 -> 15 -> 20

print("Current List:")
linked_list.traverse()  # Should print 5, 10, 15, 20
