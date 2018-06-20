class Node(object):
    def __init__(self, data, parentNode):
        self.data = data;
        self.leftChild = None;
        self.rightChild = None;
        self.balance = 0;
        self.parentNode = None;
    def insert(self, data, parentNode):
        if data < self.data:
            if not self.leftChild:
                self.leftChild = Node(data, parentNode);
            else:
                self.leftChild.insert(data, parentNode);
        else:
            if not self.rightChild:
                self.rightChild = Node(data, parentNode);
            else:
                self.rightChild.insert(data, parentNode);
        return parentNode;
    def traverseInorder(self):
        if self.leftChild is not None:
            self.leftChild.traverseInorder();

        print(self.data);

        if self.rightChild is not None:
            self.rightChild.traverseInorder();
    def getMin(self):
        if self.leftChild is not None:
            return self.leftChild.getMin();
        else:
            return self.data;
    def getMax(self):
        if self.rightChild is not None:
            return self.rightChild.getMax();
        else:
            return self.data;
class avl(object):
    def __init__(self):
        self.rootNode = None;
    def insert(self, data):
        parentNode = self.rootNode;
        if self.rootNode == None:
            parentNode  = Node(data, None);
            self.rootNode = parentNode;
        else:
            parentNode = self.rootNode.insert(data, self.rootNode);
        self.rebalanceTree(parentNode);
    def rebalanceTree(self, parentNode):

        self.setBalance(parentNode);

        if parentNode.balance > 1:
            if self.height(parentNode.leftChild.leftChild) >= self.height(parentNode.leftChild.rightChild):
                parentNode = self.rotateRight(parentNode);
            else:
                parentNode = self.rotateLeftRight(parentNode);
        elif parentNode.balance < -1:
            if self.height(parentNode.rightChild.rightChild) >= self.height(parentNode.rightChild.leftChild):
                parentNode = self.rotateLeft(parentNode);
            else:
                parentNode = self.rotateRightLeft(parentNode);
        if parentNode.parentNode is not None:
            self,rebalanceTree(parentNode.parentNode);
        else:
            self.rootNode = parentNode;

    def rotateLeftRight(self, node):
        print("rotating left then right..");
        node.leftChild = self.rotateLeft(node.leftChild);
        return self.rotateRight(node);
    def rotateRightLeft(self, node):
        print("rotating right then left...");
        node.rightChild = self.rotateRight(node.rightChild);
        return self.rotateLeft(node);
    def rotateLeft(self, node):
        print("rotating Left...");
        b = node.rightChild;
        b.parentNode = node.parentNode;
        node.rightChild =   b.leftChild;
        if node.rightChild is not None:
            node.rightChild.parentNode = node;
        b.leftChild = node;
        node.parentNode = b;
        if b.parentNode is not None:
            if b.parentNode.rightChild == node:
                b.parentNode.rightChild = b;
            else:
                b.parentNode.leftChild = b;
        self.setBalance(node);
        self.setBalance(b);
        return b;

    def rotateRight(self, node):
        print("rotate Right...");
        b = node.leftChild;
        b.parentNode = node.parentNode;
        node.leftChild = b.rightChild;
        if node.leftChild is not None:
            node.leftChild.parentNode = node;
        b.rightChild = node;
        node.parentNode = b;

        if b.parentNode is not None:
            if b.parentNode.rightChild == node:
                b.parentNode.rightChild = b;
            else:
                b.parentNode.leftChild = b;
        self.setBalance(node);
        self.setBalance(b);
        return b;

    def setBalance(self, node):
        node.balance = (self.height(node.leftChild) - self.height(node.rightChild));
        return node.balance;
    def height(self, node):
        if node == None:
            return -1;
        else:
            return 1+ max(self.height(node.leftChild), self.height(node.rightChild));
    def traverseInorder(self):
        self.rootNode.traverseInorder();

tree = avl();
tree.insert(4);
tree.insert(2);
tree.insert(3);
tree.traverseInorder();
