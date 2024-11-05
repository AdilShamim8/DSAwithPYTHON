'''
ALGORITHM PopOperation
1. Start.
2. Check if the stack is empty:
   If top index = -1:
       Print "Stack Underflow"  // Error message
       Exit operation.
3. If the stack is not empty:
   Access the data element at the position pointed by top.
4. Decrease the value of top by 1.
5. End.
'''



class Stack:
    def __init__(self, max_size):
        self.max_size = max_size  # Maximum size of the stack
        self.stack = [None] * max_size  # Initialize the stack with None
        self.top = -1  # Initialize top index to -1 (indicating an empty stack)

    def push(self, new_element):
        # Check for Stack Overflow
        if self.top == self.max_size - 1:
            print("Stack Overflow")
            return  # Exit the operation
        
        # Increment the Top Index
        self.top += 1
        
        # Add the New Element
        self.stack[self.top] = new_element
        print(f"Element {new_element} pushed to stack.")

    def pop(self):
        # Step 2: Check if the stack is empty
        if self.top == -1:
            print("Stack Underflow")  # Error message
            return None  # Exit operation
        
        # Step 3: Access the data element at top
        popped_element = self.stack[self.top]
        
        # Step 4: Decrease the value of top by 1
        self.top -= 1
        
        print(f"Element {popped_element} popped from stack.")
        return popped_element  # Return the popped element

# Example usage:
stack_size = 5
stack = Stack(stack_size)

# Pushing elements onto the stack
stack.push(10)
stack.push(20)
stack.push(30)

# Popping elements from the stack
stack.pop()  # Should pop 30
stack.pop()  # Should pop 20
stack.pop()  # Should pop 10
stack.pop()  # Should trigger stack underflow
