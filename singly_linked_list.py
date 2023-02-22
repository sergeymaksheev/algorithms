
class Cell:
    def __init__(self, value: int =None):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.top = None

    def add_to_start(self, value: int):
        new_cell = Cell(value)

        if not self.top:
            self.top = new_cell
        else:
            new_cell.next = self.top
            self.top = new_cell


    def is_empty(self):
        return self.top == None


    def add_to_end(self, value: int):
        new_cell = Cell(value)

        if self.is_empty():
            self.top = new_cell
        else:
            start = self.top
            while start.next:
                start = start.next
            start.next = new_cell


    def delete(self, value):
        if not self.is_empty():

            start = self.top
            if start.value == value:
                self.top = start.next 
                return 
            while start.next:
                if start.next.value == value:
                    start.next = start.next.next
                    return
                start = start.next

 


        




    def search_value(self, value):
        if self.is_empty():
            return False

        start = self.top
        while start:
            if start.value == value:
                return True
            start = start.next

        return False

    def print_list(self):
        if not self.is_empty():
            start = self.top

            while start:
                print(start.value)
                start = start.next


mylist = SinglyLinkedList()
mylist.add_to_start(1)
mylist.add_to_start(2)
mylist.add_to_start(3)
mylist.add_to_start(4)
mylist.add_to_start(5)
mylist.add_to_start(6)
mylist.add_to_start(7)