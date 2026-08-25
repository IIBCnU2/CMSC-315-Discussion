"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # A list stores the stack values. The end of the list represents the top.
        self.items = []

    def push(self, value):
        # Adding to the end allows the most recently added item to be removed first,
        # which provides LIFO (Last In, First Out) behavior.
        self.items.append(value)

    def pop(self):
        # Remove and return the most recently added value.
        if self.is_empty():
            raise IndexError("Cannot pop from an empty stack.")
        return self.items.pop()

    def peek(self):
        # Peek returns the top value without removing it from the stack.
        if self.is_empty():
            raise IndexError("Cannot peek at an empty stack.")
        return self.items[-1]

    def is_empty(self):
        # Return True when the stack contains no values.
        return len(self.items) == 0


class Queue:
    def __init__(self):
        # deque allows efficient additions at the back and removals from the front.
        self.items = deque()

    def enqueue(self, value):
        # Add the value to the back of the queue.
        # The first value added will be the first value removed,
        # providing FIFO (First In, First Out) behavior.
        self.items.append(value)

    def dequeue(self):
        # Remove and return the value at the front of the queue.
        if self.is_empty():
            raise IndexError("Cannot dequeue from an empty queue.")
        return self.items.popleft()

    def front(self):
        # Return the front value without removing it from the queue.
        if self.is_empty():
            raise IndexError("Cannot view the front of an empty queue.")
        return self.items[0]

    def is_empty(self):
        # Return True when the queue contains no values.
        return len(self.items) == 0


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.


print("\n=== STACK DEMO ===")

    stack = Stack()

    print("Adding four values to the stack...")
    stack.push("First")
    stack.push("Second")
    stack.push("Third")
    stack.push("Fourth")

    print("The stack uses LIFO: Last In, First Out.")
    print("Top value:", stack.peek())

    print("\nRemoving values from the stack:")
    print("Popped:", stack.pop())
    print("Popped:", stack.pop())
    print("Popped:", stack.pop())
    print("Popped:", stack.pop())

    print("Is the stack empty?", stack.is_empty())

    # Test popping from an empty stack
    print("\nTesting pop() on an empty stack:")
    try:
        stack.pop()
    except IndexError as error:
        print("Error:", error)

    # Test peeking at an empty stack
    print("\nTesting peek() on an empty stack:")
    try:
        stack.peek()
    except IndexError as error:
        print("Error:", error)

    # Single-item stack test
    print("\nTesting a stack with one item:")
    single_stack = Stack()
    single_stack.push("Only Item")

    print("Before removal, is the stack empty?",
          single_stack.is_empty())

    print("Removing:", single_stack.pop())

    print("After removal, is the stack empty?",
          single_stack.is_empty())

# ===============================
# TODO (Student): QUEUE DEMO
# ===============================
# Requirements:
# 1. Create a Queue object.
# 2. Add at least 4 values to the queue.
# 3. Improve the print statements so they clearly explain what is happening.
# 4. Demonstrate FIFO behavior.
# 5. Show what happens when dequeue() is used on an empty queue.
#
# Edge Cases:
# 6. Show what happens when front() is used on an empty queue.
# 7. Create a queue with only one item, remove it,
#    and verify the queue is empty afterward.

print("\n=== QUEUE DEMO ===")

    queue = Queue()

    print("Adding four values to the queue...")
    queue.enqueue("First")
    queue.enqueue("Second")
    queue.enqueue("Third")
    queue.enqueue("Fourth")

    print("The queue uses FIFO: First In, First Out.")
    print("Front value:", queue.front())

    print("\nRemoving values from the queue:")
    print("Dequeued:", queue.dequeue())
    print("Dequeued:", queue.dequeue())
    print("Dequeued:", queue.dequeue())
    print("Dequeued:", queue.dequeue())

    print("Is the queue empty?", queue.is_empty())

    # Test dequeuing from an empty queue
    print("\nTesting dequeue() on an empty queue:")
    try:
        queue.dequeue()
    except IndexError as error:
        print("Error:", error)

    # Test viewing the front of an empty queue
    print("\nTesting front() on an empty queue:")
    try:
        queue.front()
    except IndexError as error:
        print("Error:", error)

    # Single-item queue test
    print("\nTesting a queue with one item:")
    single_queue = Queue()
    single_queue.enqueue("Only Item")

    print("Before removal, is the queue empty?",
          single_queue.is_empty())

    print("Removing:", single_queue.dequeue())

    print("After removal, is the queue empty?",
          single_queue.is_empty())


if __name__ == "__main__":
    main()
