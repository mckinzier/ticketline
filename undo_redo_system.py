# Import the Node class you created in node.py
from node import Node

# Implement your Stack class here
class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None
    
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            return None
        popped_value = self.top.value
        self.top = self.top.next
        return popped_value

    def peek(self):
        if self.is_empty():
            return None
        return self.top.value

    def print_stack(self):
        current = self.top
        while current:
            print(current.value)
            current = current.next

def run_undo_redo():
    # Create instances of the Stack class for undo and redo
    undo_stack = Stack()
    redo_stack = Stack()

    while True:
        print("\n--- Undo/Redo Manager ---")
        print("1. Perform action")
        print("2. Undo")
        print("3. Redo")
        print("4. View Undo Stack")
        print("5. View Redo Stack")
        print("6. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            action = input("Describe the action (e.g., Insert 'a'): ")
            # Push the action onto the undo stack and clear the redo stack
            undo_stack.push(action)
            redo_stack = Stack()

            print(f"Action performed: {action}")


        elif choice == "2":
            # Pop an action from the undo stack and push it onto the redo stack
            action = undo_stack.pop()
            if action is not None:
                redo_stack.push(action)
                print(f"Action undone: {action}")
            else:
                print("Nothing to undo.")
            

        elif choice == "3":
            # Pop an action from the redo stack and push it onto the undo stack
            action = redo_stack.pop()
            if action is not None:
                undo_stack.push(action)
                print(f"Action redone: {action}")
            else:
                print("Nothing to redo.")


        elif choice == "4":
            # Print the undo stack
            print("\nUndo Stack:")
            undo_stack.print_stack()
            

        elif choice == "5":
            # Print the redo stack
            print("\nRedo Stack:")
            redo_stack.print_stack()
            
            
        elif choice == "6":
            print("Exiting Undo/Redo Manager.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    run_undo_redo()



def test_stack():
    stack = Stack()

    """test pushing"""
    stack.push("Action 1")
    stack.push("Action 2")
    stack.push("Action 3")

    """test peeking"""
    assert stack.peek() == "Action 3"

    """test popping"""
    assert stack.pop() == "Action 3"

    """test peeking after popping"""
    assert stack.peek() ==  "Action 2"

    """test printing stack"""
    stack.print_stack()  # Should print Action 2, Action 1

    """remove all items"""
    assert stack.pop() == "Action 2"
    assert stack.pop() == "Action 1"

    """test popping from empty stack"""
    assert stack.pop() is None

    print("All tests passed.")

