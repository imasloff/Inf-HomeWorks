class Element:
    def __init__(self):
        self.data = None
        self.prev = None


class Stack:
    def __init__(self):
        self.cur_top = None
        self.size = 0

    def push(self, data):
        new_top = Element()
        new_top.data = data
        new_top.prev = self.cur_top
        self.cur_top = new_top
        self.size += 1

    def pop(self):
        old_top = self.cur_top
        if old_top is None:
            print("Error: stack is empty!")
            return None
        self.cur_top = old_top.prev
        self.size -= 1
        return old_top.data

    def stack_print(self):
        p_elem = self.cur_top
        while p_elem:
            print (str(p_elem.data))
            p_elem = p_elem.prev

    def top(self):
        if self.cur_top is None:
            print("Error: stack is empty!")
            return None
        return self.cur_top.data

    def get_size(self):
        return self.size

    def clear(self):
        self.cur_top = None
        self.size = 0
