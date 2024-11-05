'''
Algorithm: QDELETE(QUEUE, N, FRONT, REAR, ITEM)

1. Check if Queue is Empty
    • If FRONT = NULL, the queue is empty:
        • Print “UNDERFLOW” (indicating no items to delete).
        • Exit the function.
        
2. Retrieve the Front Item
    • Set ITEM = QUEUE[FRONT] (the item to delete is at the front).
    
3. Adjust the FRONT Position
    • If FRONT = REAR (only one item in the queue):
        • Set FRONT = NULL and REAR = NULL (the queue is now empty).
    • Else if FRONT = N (end of the queue array):
        • Set FRONT = 1 (move FRONT to the beginning for a circular queue).
    • Else:
        • Set FRONT = FRONT + 1 (move FRONT to the next position).
        
4. End of Procedure
    • Return from the function.

'''





class Queue:
    def __init__(self, maxSize):
        self.queue = [None] * maxSize
        self.front = -1
        self.rear = -1
        self.maxSize = maxSize

    def enqueue(self, element):
        if self.rear == self.maxSize - 1:
            print("Queue is full")
            return
        if self.front == -1:
            self.front = 0
        self.rear += 1
        self.queue[self.rear] = element
        print(f"Inserted {element} into the queue")

    def dequeue(self):
        # Check if the queue is empty
        if self.front == -1 or self.front > self.rear:
            print("Queue is empty")
            return

        # Retrieve and remove the front item
        item = self.queue[self.front]
        self.front += 1
        print(f"Deleted item: {item}")

        # Reset front and rear if the queue is now empty
        if self.front > self.rear:
            self.front = -1
            self.rear = -1

# Example usage
queue = Queue(5)
queue.enqueue(10)
queue.enqueue(20)
queue.dequeue()  # Output: Deleted item: 10
queue.dequeue()  # Output: Deleted item: 20
queue.dequeue()  # Output: Queue is empty
