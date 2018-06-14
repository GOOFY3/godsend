class Node(object):
    def __init__(self, data):
        self.data = data;
        self.leftChild = None;
        self.rightChild = None;
    def insert(self,data):
        if data < self.data:
            if not self.leftChild:
                self.leftChild = Node(data);
            else:
                self.leftChild.insert(data);
        else:
            if not self.rightChild:
                self.rightChild = Node(data);
            else:
                self.rightChild.insert(data);
    def getMin(self):
        if not self.leftChild:
            return self.data;
        else:
            return self.leftChild.getMin();
    def getMax(self):
        if not self.rightChild:
            return self.data;
        else:
            return self.rightChild.getMax();
    def traverseInorder(self):
        if self.leftChild is not None:
            self.leftChild.traverseInorder();

        print(self.data);

        if self.rightChild is not None:
            self.rightChild.traverseInorder();
    def remove(self, data):
        if data < self.data:
            self.leftChild.remove(data);
        elif data > self.data:
            self.rightChild.remove(data);
        else:
            if self.leftChild is None:
                temp = self.rightChild;
                self = None;
                return temp;
            elif self.rightChild is None:
                temp = self.leftChild;
                self = None;
                return temp;
            temp = self.rightChild.getMin();
            self.data = temp.data;
            self.rightChild  = self.rightChild.remove(temp.data);
        return self;

class BST(object):
    def __init__(self):
        self.rootNode = None;
    def insert(self, data):
        if not self.rootNode:
            self.rootNode = Node(data);
        else:
            self.rootNode.insert(data);
    def remove(self, data):
        if self.rootNode is not None:
            return self.rootNode.remove(data);
    def getMax(self):
        if self.rootNode:
            return self.rootNode.getMax();
    def getMin(self):
        if self.rootNode:
            return self.rootNode.getMin();
    def traverseInorder(self):
        if self.rootNode:
            return self.rootNode.traverseInorder();

bst = BST();
bst.insert(50);
bst.insert(30);
bst.insert(20);
bst.insert(40);
bst.insert(70);
bst.insert(60);
bst.insert(80);

bst.traverseInorder();

print("removing!!");
bst.remove(40);

bst.traverseInorder();
