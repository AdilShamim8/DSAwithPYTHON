'''
Algorithm: QINSERT(QUEUE, N, FRONT, REAR, ITEM)

1. Check if Queue is Full
    • If FRONT = 1 and REAR = N (the queue is completely filled), or if FRONT = REAR + 1 (circular queue is full), then:
        • Print “OVERFLOW” (no more items can be added).
        • Exit the function.
        
2. Find New Position for REAR
    • If FRONT = NULL (queue is initially empty):
        • Set FRONT = 1 and REAR = 1.
    • Else if REAR = N (end of the queue array):
        • Set REAR = 1 (move to the beginning for circular queue).
    • Else:
        • Set REAR = REAR + 1 (move to the next position).
        
3. Insert ITEM at REAR
    • Set QUEUE[REAR] = ITEM (insert the new element).
    
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
        # Check if the queue is full
        if self.rear == self.maxSize - 1:
            print("Queue is full")
            return

        # Insert the first element
        if self.front == -1:
            self.front = 0

        # Increment rear and add the new element
        self.rear += 1
        self.queue[self.rear] = element
        print(f"Inserted {element} into the queue")

# Example usage
queue = Queue(5)
queue.enqueue(10)  # Output: Inserted 10 into the queue
queue.enqueue(20)  # Output: Inserted 20 into the queue
queue.enqueue(30)  # Output: Inserted 20 into the queue
queue.enqueue(20)  # Output: Queue is full
queue.enqueue(40)  # Output: Queue is full
queue.enqueue(50)  # Output: Queue is full



