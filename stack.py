class Element:
    def __init__(self):
        self.data = None
        self.prev = None


class Stack:
    def __init__(self):
        self.cur_top = None

    def push(self, data):
        new_top = Element()
        new_top.data = data
        new_top.prev = self.cur_top
        self.cur_top = new_top

    def pop(self):
        old_top = self.cur_top
        self.cur_top = old_top.prev
        return old_top

    def stack_print(self):
        p_elem = self.cur_top
        while p_elem:
            print (str(p_elem.data))
            p_elem = p_elem.prev

    def top(self):
        return self.cur_top.data

    def size(self):
        tmp = self.cur_top
        count = 0
        while tmp is not None:
            count += 1
            tmp = tmp.prev

        return count

    def clear(self):
        tmp = self.cur_top
        while tmp is not None:
            self.cur_top = None
            tmp = tmp.prev

s1 = Stack()

s1.push(1)
s1.push("Ivan")
s1.push(3)

s1.stack_print()

print("size - " + str(s1.size()))

print("top - " + str(s1.top()))
s1.pop()
s1.stack_print()
print("newtop - " + str(s1.top()))
s1.pop()
print("newtop2 - " + str(s1.top()))
s1.pop()

print("size - " + str(s1.size()))

s1.push(1)
s1.push("Ivan")
s1.push(3)

s1.stack_print()

s1.clear()
print("size - " + str(s1.size()))
s1.stack_print()
