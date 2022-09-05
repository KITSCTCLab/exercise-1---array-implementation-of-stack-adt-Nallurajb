import os
class Stack:
    def __init__(self, size):
        self.items = []
        self.size = size

    def is_empty(self):
        # Write code here
        if len(self.items)==0:
            return True
        else:
            return False

    def is_full(self):
        # Write code here
        if len(self.items)==self.size:
            return True
        else:
            return False

    def push(self, data):
        if not self.is_full():
            # Write code here
            self.items.append(data)

    def pop(self):
        if not self.is_empty():
            # Write code here
            self.items.pop()

    def status(self):
        # Write code here
        for element in self.items:
            print(element)
