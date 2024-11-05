'''
ALGORITHM PushOperation
1. Start.
2. Check for Stack Overflow:
   If top index = maximum size - 1:
       Print "Stack Overflow"
       Exit operation.
3. Increment the Top Index:
   Set top = top + 1.
4. Add the New Element:
   Set stack[top] = newElement.
5. End.
'''




class Stack:
    def __init__(self, max_size):
        self.max_size = max_size  # Maximum size of the stack
        self.stack = [None] * max_size  # Initialize the stack with None
        self.top = -1  # Initialize top index to -1 (indicating an empty stack)

    def push(self, new_element):
        # Step 2: Check for Stack Overflow
        if self.top == self.max_size - 1:
            print("Stack Overflow")
            return  # Exit the operation
        
        # Step 3: Increment the Top Index
        self.top += 1
        
        # Step 4: Add the New Element
        self.stack[self.top] = new_element
        print(f"Element {new_element} pushed to stack.")

# Example usage:
stack_size = 5
stack = Stack(stack_size)

# Pushing elements onto the stack
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)
stack.push(60)  # This will trigger stack overflow
