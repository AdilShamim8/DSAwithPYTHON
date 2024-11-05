'''
ALGORITHM DeleteNodeByValue
1. Start.
2. If head is null, print "List is empty." and exit.
3. If head.data is equal to value:
    a. Set head to head.next.  // Remove the head node
4. Set current to head.
5. While current.next is not null:
    a. If current.next.data is equal to value:
        i. Set current.next to current.next.next.  // Bypass the node
        ii. Exit.
    b. Set current to current.next.
6. Print "Value not found in the list."
7. End.
'''




class Node:
    def __init__(self, data):
        self.data = data  # Store data
        self.next = None  # Pointer to the next node

class SinglyLinkedList:
    def __init__(self):
        self.head = None  # Initialize head to None

    # Insertion at the end (for testing purposes)
    def insert_at_end(self, data):
        new_node = Node(data)  # Create a new node
        if self.head is None:  # Check if the list is empty
            self.head = new_node  # Make this node the head
            return
        
        current = self.head
        while current.next is not None:  # Traverse to the last node
            current = current.next
        
        current.next = new_node  # Link the last node to the new node

    # Deleting a node by value
    def delete_node_by_value(self, value):
        if self.head is None:  # Check if the list is empty
            print("List is empty.")
            return

        if self.head.data == value:  # Check if the head is the value to delete
            self.head = self.head.next  # Remove head node
            return

        current = self.head
        while current.next is not None:
            if current.next.data == value:  # Found the node to delete
                current.next = current.next.next  # Bypass the node
                return
            current = current.next
        print("Value not found in the list.")

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
linked_list.insert_at_end(30)  # List: 10 -> 20 -> 30

print("Current List:")
linked_list.traverse()  # Should print 10, 20, 30

linked_list.delete_node_by_value(20)  # Delete node with value 20
print("List after deletion of 20:")
linked_list.traverse()  # Should print 10, 30

linked_list.delete_node_by_value(40)  # Attempt to delete a non-existing value
