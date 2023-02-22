
class Cell:
    def __init__(self, value: int =None):
        self.value = value
        self.next = None


class SinglyLinkedListWithTail:
    def __init__(self):
        self.top = None
        self.tail = None

    def add_to_front(self, value: int):
        new_cell = Cell(value)

        if not self.top:
            self.top = new_cell
            self.tail = new_cell
        else:
            new_cell.next = self.top
            self.top = new_cell


    def add_to_back(self, value: int):
        new_cell = Cell(value)

        if not self.top:
            self.top = new_cell
            self.tail = new_cell
        else:
            self.tail.next = new_cell
            self.tail = new_cell


    def is_empty(self):
        return self.top == None
    

    def delete(self, value):
        if self.is_empty():
            return False
        elif not self.is_empty():
            start = self.top
            if start.value == value:
                self.top = start.next
            else:
                while start and start.next:
                    if start.next.value == value:
                        start.next = start.next.next
                        start = start.next


    def print_list(self):
        if not self.is_empty():
            start = self.top

            while start:
                print(start.value)
                start = start.next

mylist = SinglyLinkedListWithTail()