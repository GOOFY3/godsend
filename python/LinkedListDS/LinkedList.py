from LinkedListDS.Node import Node;

class LinkedList(object):
    def _init_(self):
        self.head = None;
        self.counter = 0;

    def traverseList(self):
        actualNode = self.head;

        while actualNode is not None:
            print("%d" % actualNode.data);
            actualNode = actualNode.nextNode;

    def insertStart(self, data):
        newNode = Node(data);
        self.counter += 1;

        if not self.head:
            self.head = newNode;
        else:
            newNode.nextNode = self.head;
            self.head = newNode;

    def size(self):
        return self.counter;

    def remove(data):
        if self.head:
            if data == self.head.data:
                self.head = self.head.nextNode;
            else:
                self.head.remove(data, self.head);
