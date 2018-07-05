class Node(object):
    def __init__(self, name):
        self.name = name;
        self.adjacentList = [];
        self.visited = False;

    def dfs(node):
        node.visited = True;
        print("%s -->" %node.name);
        for n in node.adjacentList:
            if not n.visited:
                n.dfs();

node1 = Node("A");
node2 = Node("B");
node3 = Node("C");
node4 = Node("D");
node5 = Node("E");


node1.adjacentList.append(node2);
node1.adjacentList.append(node3);
node2.adjacentList.append(node4);
node4.adjacentList.append(node5);

Node.dfs(node1);
