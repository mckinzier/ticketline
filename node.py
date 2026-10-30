# Implement your Node class here
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None



"""
Code Response
--------------
Why is a stack the right choice for undo/redo?
Why is a queue better suited for the help desk?
How do your implementations differ from Python’s built-in lists?

Stack is the right choice for redo/undo because it uses a last in and firstt out principle. 
They are supposed to be used when you want the most recent adding item to be accessed first.
They allow you to reverse, and redo operations which is exactly what we needed for redo/undo scenario.
Stacks use a top pinter to keep track of the last item added to the stack and removes it first when you use pop.
A que is better suited for a help desk because customers are helped in the order of their tickets. First come, first served.
New people are added to the end of a queue like you would see in a line at a store. It is a fair process that makes sure 
people are helped in the order they arrived. Its like a waitlist in a restuarant. Queues use a front and rear pointer to keep 
track of the first and last items in the queue. My implementions differ from Python's build in lists because I created nodes 
and pointers that you don't hae to worry about using lists. Each node holds a value and a pointer to the next node. My stack 
uses a top pointer to keep track of the last item added to the stack. My queue uses a front and rear pointer to keep track of 
the first and last items in the queue.
"""