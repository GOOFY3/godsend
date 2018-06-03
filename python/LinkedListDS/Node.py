
# creating a node
class Node(object):
    def _init_(self, data):
        self.data = data;
        self.nextNode = None;

# removing a node
    def remove(self, data, previousNode):
        if self.data = data:
            previousNode.nextNode = self.nextNode;
            del self.data;
            del self.nextNode;
        else:
            if self.nextNode is not None:
                self.nextNode.remove(data, self);            
