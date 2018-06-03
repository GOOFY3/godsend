class Node(object):
    def __init__(self,data,next_node=None):
        self.data = data;
        self.next_node = next_node;
    def set_data(self,val):
        self.data = val;
    def get_data(self):
        return self.data;
    def set_next(self,val):
        self.next_node = val;
    def get_next(self):
        return self.next_node;

class LinkedList(object):
    def __init__(self,head=None):
        self.head = None;
        self.size = 0;
    def get_size(self):
        return self.size;
    def insert(self, data):
        newNode = Node(data,self.head);
        self.size+=1;
        self.head = newNode;
        return True;
    def printList(self):
        current = self.head;
        while current:
            print(current.data);
            current = current.next_node;

    # def remove(self, data, previousNode):
    #     prev = None;
    #     current = self.head;
    #     while current:
    #         if current.data == data:
    #
    #         else:
    #             current = current.next_node;

myList = LinkedList()
print("Inserting:")
print(myList.insert(5))
print(myList.insert(12))
print(myList.insert(15))
print(myList.insert(2))
print(myList.insert(3))
print("Printing:")
print(myList.printList())
print("Size")
print(myList.get_size())
